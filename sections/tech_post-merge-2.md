> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> Specifically: the register extent it names is a snapshot and has since grown;
> read §4.7's register in the master for the live list.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-2 addendum (tech-director)

> **Read this first.** `sections/tech.md` is marked **APPLIED ADDENDUM — do not
> re-apply**; its nine replacement pairs are already in the master and its Old
> blocks no longer match. This file supersedes nothing in it and does not touch
> it. Every passage below is an exact old→new replacement against
> `source/gdd.md` (md5 `0eedea2dfd7b17a508e162427682ce64`). Anything in this
> file that is not inside an Old/New pair is commentary for the Director and is
> **not** meant to be merged — which is precisely the mistake that produced the
> violation this addendum fixes.

## Placement

- **Amendment A — §4.7 Spec Stub 7, invariant T-SCN-06.** Fixes the
  `dead-reference` violation: the pointer `see the note above the stub` resolves
  to nothing in the master, because the note it names lived only in
  `sections/tech.md`'s Amendment 3 commentary and was never merged. The
  reasoning is folded into T-SCN-06 and the pointer is dropped. **Required.**
- **Amendment B — §4.11, the critical-path paragraph.** One phrase, `week-2
  vertical-slice integration gate`, is stale since the Director's Q23 ruling
  moved the vertical slice to week 3. Not the gate's violation, not a re-filing
  of the schedule contradiction — a two-word deletion that makes §4.11 quote
  Q20's own wording. **Director's option; independently applicable.**

Nothing else in §4.7–§4.11 changes. No Q number is filed; the register stays
**Q1–Q23**. Q20, Q21 and Q22 remain open and untouched by this addendum.

### Why fold, rather than merge the note above the stub

The gate offered both. Folding wins on one argument: §4.7 is an unbroken run of
fenced spec blocks from Stub 1 to Stub 8 with no interleaved prose, so a note
between Stub 6 and Stub 7 would be the only paragraph of its kind in the
section — the easiest thing in the document for a future merge to drop, reorder
or land in the wrong gap. It would also leave the citation a *citation*: a
pointer whose target is a position ("above the stub") rather than a name. That
pointer has now failed once. A self-contained invariant cannot dangle, and the
reasoning is about how T-SCN-06 is written, so T-SCN-06 is where it belongs.

The cost is honest and worth stating: T-SCN-06 grows from 18 lines to 29 and is
now by some distance the longest invariant in §4. It is also the only one whose
*shape* — quantifying over a named hex rather than searching for any qualifying
one — is a decision a reimplementer could silently get backwards. Length here
buys a gate that cannot be rewritten wrong.

## Draft

### Amendment A — §4.7 Stub 7, T-SCN-06 (the dead reference)

The dropped note said this: §2.13.1 states an **existential** ("at least one
Infantry deployment hex must have a land path…") *and* a **naming** requirement
("the scenario file names that unit… so the turn-1a *marked* Infantry is the one
already standing on the lane"). Asserting the existential **over the named hex**
collapses both into one check. Written the other way — find any qualifying hex,
then compare it to the named one — the validator passes a map whose qualifying
lane belongs to a unit §2.11.6 turn 1a never marks. That is a real bug class,
not a style preference, and it is the load-bearing justification for how the
gate is written, so it goes in the document rather than in a section file.

Two edits to the note as it becomes GDD prose:

1. The original ended "…which is the exact class of bug the §2.11.6 violation
   was." That cites a *gate run*, not the document — merging it verbatim would
   trade one dead reference for another. The replacement names the failure in
   terms a reader of the GDD can check: the reachability rule satisfied to the
   letter while the marked Infantry stands somewhere else.
2. `§2.11.6 turn 1a` is written out rather than left as "turn 1a", so the
   sentence resolves without the surrounding paragraph.

**Old** (inside `SPEC STUB 7`, invariant `T-SCN-06`):

```
            first lesson uncontested rather than a crossing. Asserting the
            existential over the NAMED hex is deliberate — see the note above
            the stub. The gate asserts ARRIVAL ONLY: the turn the tile flips is
```

**New:**

```
            first lesson uncontested rather than a crossing. Asserting the
            existential over the NAMED hex is deliberate. §2.13.1 states an
            EXISTENTIAL ("at least one Infantry deployment hex must have a
            land path...") and, alongside it, a NAMING requirement (the
            scenario file names that unit, so §2.11.6's turn-1a marked
            Infantry is the one already standing on the lane); quantifying
            over the named hex collapses both into a single check. Written
            the other way round — find ANY qualifying hex, then compare it to
            the named one — the validator passes a map whose qualifying lane
            belongs to a unit turn 1a never marks: the reachability rule
            satisfied to the letter while the marked Infantry stands
            somewhere else, and the guided opening's first directive walking
            the player down a lane nobody priced.
            The gate asserts ARRIVAL ONLY: the turn the tile flips is
```

Everything before and after these three lines is unchanged, including
T-SCN-06's derived-ceiling clause, its Bridge exclusion, and its closing
`"capturing by turn 2, never captured by turn 2."` T-SCN-05 (not mine),
T-SCN-07 and T-SCN-08 are untouched, and nothing is renumbered.

### Amendment B — §4.11, the stale `vertical-slice` phrase (Director's option)

Q23 ruled the vertical slice into week 3; §4.4 now reads "Week 2 … **Move +
attack only** — no capture, no production, no AI opponent." §4.11's critical-path
paragraph still calls T-INT-02 "the week-2 vertical-slice integration gate,"
which now welds a week-2 thing to a week-3 thing. The integration gate itself is
still week 2 — §4.4 week 2 is the engine-presentation week and includes "the one
scenario loading, validating and rendering" — so the fix is to delete
`vertical-slice` and nothing else. This is not a re-filing of the schedule
contradiction: it makes §4.11 read exactly as Q20's own row already reads
("the week-2 integration gate (T-INT-02) and the week-4 self-play logs
(T-SAVE-07)"), so the two places that describe the same sequencing stop
disagreeing about which milestone T-INT-02 belongs to.

**Old** (§4.11, final paragraph):

```
week too late in one respect: the *format and headless replayer* are the
instrument for the week-2 vertical-slice integration gate (T-INT-02) and the
week-4 self-play logs (T-SAVE-07). Splitting the row — format + replayer early,
```

**New:**

```
week too late in one respect: the *format and headless replayer* are the
instrument for the week-2 integration gate (T-INT-02) and the week-4
self-play logs (T-SAVE-07). Splitting the row — format + replayer early,
```

If the Director prefers to leave §4.11 alone until Q20 is ruled — Q20 rewrites
this sentence anyway — skipping Amendment B costs nothing except that the phrase
stays wrong in the meantime. Amendment A does not depend on it.

### The related check: every pointer-style citation in the merged §4.7–§4.11

The Director asked whether any *other* citation in my merged sections points at
commentary that did not come with it. I checked all of §4.7–§4.11 for citations
whose target is a **position** ("above", "below", "the note", "see") or an
**artifact outside the GDD**, since those are the two ways a reference can die
in a merge. Result: **one dead reference (the violation), one stale phrase
(Amendment B), everything else resolves.**

| Citation | Location | Target | Verdict |
|---|---|---|---|
| `see the note above the stub` | §4.7 T-SCN-06 | commentary that never merged | **DEAD** — Amendment A |
| `the week-2 vertical-slice integration gate` | §4.11 critical path | §4.4 wk 2, which no longer holds the slice | **STALE** since Q23 — Amendment B |
| `Q1–Q23, Open questions below` | §4.7 preamble | the register, same subsection | Resolves; extent is correct post-Q23 |
| `stubs 1–8 below are also the build-order row numbers` | §4.7 conventions | §4.11 rows 1–8 | Resolves |
| `the discipline that appended `type` last in the combat addendum, Part A` | §4.7 Stub 7 `scenarioHash` | `combat_spec_addendum.md`, named in §3's ledger paragraph | Resolves — external, but §3 names the artifact and the commit (`5ffa8d6`) |
| `addendum Part A` ×3 | §4.8 `Type` row, `EUnitType` note, effectiveness schema | same | Resolves, same grounds |
| `the effectiveness table below` | §4.8 `EUnitType` note | §4.8 Type-effectiveness schema, 16 lines later | Resolves |
| `guidedOpening` field description's two design decisions | §4.7 Stub 7 | in-block: T-SCN-02 uniqueness, side-enumeration hash order | **Survived** — both merged inside the field block, as the Director suspected; neither is a pointer |
| `§2.11.6 turn 1a` ×2 | §4.7 Stub 7 field + T-SCN-07 | §2.11.6-B beat 1a | Resolves — the beat is labelled `1a` in the merged table |
| `§2.11.5` screen list, `§2.11.8` build ranking | §4.10 save-slot policy | both subsections exist; §2.11.5 ends "That is the complete screen list" with no save surface | Resolves; the claim is still true of the merged §2.11 |
| `T-DATA-03's single CanCapture row` | §4.7 T-SCN-06/07 | §4.8 T-DATA-03 | Resolves |
| `Longwater March, §2.13.1` | §4.7 T-SCN-08 | §2.13.1's lane table | Resolves **today** — see Handoffs for the pending interaction |
| `(§2.13.1)` symmetry-flag clause | §4.7 T-SCN-08 | §2.13.1's closing paragraph, which states the same odd-r argument | Resolves |
| `the tripwire of this stub` ×2 | §4.9 T-INT-02, §4.10 T-SAVE-05 | self-contained parentheticals | Not pointers |

The general lesson, offered once and not repeated: the two references that died
are the only two in §4 whose target was a *place* rather than a *name*. Every
citation that survived merge names a section number, a test ID, a field, or a
commit. That is a cheap rule to hold to in future addenda.

## Build order

Unchanged. This addendum adds no system, no dependency and no test ID; §4.11's
rows 1–10 stand exactly as merged. The one row it touches in substance:

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (§4.7 Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..08 |

T-SCN-06's *text* grows; its inputs, its ceiling, its determinism inheritance
and its acceptance set are byte-for-byte the same rule. Nothing that was gated
becomes ungated, and no ledger row changes status. The §3 ledger's eight
`*pending*` rows remain `*pending*`: `Source/` is still the stock Unreal
template, and the only green rows are still Combat, its test suite, Repair and
Type-effectiveness at `5ffa8d6` (17/17).

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | None | Amendment A is inside my own §4.7 and Amendment B inside my own §4.11. The one adjacent risk — §2.13.1's lane table — belongs to `scenario-designer`, who is already working it; filing a CR against a table that is mid-revision would collide with their draft. Recorded under Handoffs instead. |

## Open questions for the Director

**None new.** The fold invents no rule: every clause in the new T-SCN-06 text
restates what §2.13.1 already says (the existential, the naming requirement) or
what T-SCN-06 already asserted (quantification over the named hex). The register
stays **Q1–Q23**.

Two standing items this addendum brushes against without touching:

- **Q21** (lane measured on terrain alone vs. as deployed) still governs
  whether T-SCN-06's *numbers* are right. Amendment A changes how the invariant
  is justified, not how it prices. If Q21 is ruled "as deployed," T-SCN-06's
  reasoning survives verbatim and only the cost model moves.
- **Q22** (uncontested vs. merely reachable) is still the reason T-SCN-07 stops
  at distinctness. Untouched.

## Handoffs

- **`scenario-designer` — the T-SCN-08 fixture, and whether it survives.**
  Asked directly: **the invariant survives unconditionally; the fixture survives
  only if *Longwater March*'s two lanes remain (a) unequal and (b) both ≤ 6 MP.**
  T-SCN-08's passing fixture is "a mirror-declared scenario whose lanes cost 3
  and 4 PASSES and reports both numbers." The load-bearing property is the
  *inequality under a declared mirror* — that is the whole demonstration that
  the symmetry flag cannot substitute for a measurement. The integers 3 and 4
  are illustrative of it. So:
  - Lanes move to some other unequal pair, both ≤ 6 (say 4 and 5): the fixture
    survives in substance, and only the two numerals in T-SCN-08 need updating,
    alongside §2.13.1's table. One replacement pair, trivially.
  - Lanes come out **equal** in axial — the plausible outcome if the symmetry
    finding is that *Longwater* is a truer mirror than the odd-r ASCII made it
    look: the fixture **dies**. Not the invariant, the fixture. T-SCN-08 would
    then be citing the one map that no longer exhibits the phenomenon, and
    §2.13.1's closing argument ("*Longwater March*: 3 MP west, 4 MP east") loses
    its example at the same moment. Those two must move together or the document
    contradicts itself; whichever map still prices its two seats unequally
    becomes the fixture, and if none does, the fixture becomes a synthetic
    scenario the way the failing 7/7 case already is.
  - Either lane exceeds 6 MP: that is not a fixture problem, it is a **T-SCN-06
    failure** — the map stops satisfying §2.13.1's opening-capture reachability
    at all, and the gate is doing its job.

  I have **not** changed T-SCN-08, as instructed. The decoupled wording that
  would make it immune to the numbers — *"a mirror-declared scenario whose two
  lanes cost DIFFERENT integers passes and reports both"* — is recorded here as
  a standby only, deliberately **not** written as a replacement pair, so it
  cannot be applied by accident before the lane table settles.
- **`rules-designer`** — no interaction. Nothing here touches §2.7 capture,
  §2.8 tiebreak, or the Fame apparatus.
- **`ux-onboarding-designer`** — no edit needed, but worth knowing: the new
  T-SCN-06 text now cites §2.11.6's turn-1a beat by name as the thing the gate
  protects. If the beat is ever renumbered, T-SCN-06 and §2.13.1 both follow.
  That is a name, not a position, so it will fail loudly rather than silently.
- **Director / merge** — Amendment A is required to clear the violation;
  Amendment B is optional and independent. Applying B before Q20 is ruled is
  safe; Q20's eventual ruling rewrites that sentence regardless.

## Grounding

| Claim | Backed by |
|---|---|
| The `see the note above the stub` pointer resolves to nothing | `source/gdd.md` §4.7: Stub 6's fence closes at the line immediately preceding Stub 7's opening fence; no prose intervenes |
| The dropped note's exact reasoning | `sections/tech.md`, Amendment 3 commentary — the paragraph beginning "The gate-design decision that matters" |
| §2.13.1 states an existential *and* a naming requirement | `source/gdd.md` §2.13.1, **Opening-capture reachability** bullet: "at least one Infantry deployment hex must have a land path… The scenario file names that unit and that factory (`guidedOpening.infantry`, `guidedOpening.objective`, §4.7 Stub 7) so the turn-1a *marked* Infantry is the one already standing on the lane." |
| §2.11.6 turn 1a marks exactly one Infantry | `source/gdd.md` §2.11.6-B, beat `1a`: "Only one marked Infantry selectable; others dimmed" |
| The `guidedOpening` field's two design decisions did merge | `source/gdd.md` §4.7 Stub 7 field block: "A hex identifies the placement uniquely because T-SCN-02 already forbids two placements sharing one…" and "Entries serialize in the module's side enumeration order, not authoring order, so the hash is content-only." |
| Q23 moved the vertical slice to week 3; week 2 is move + attack | `source/gdd.md` §4.4 milestone table wk 2 and wk 3, plus the "On weeks 2–3 (Q23, ruled)" paragraph |
| Q20's row already says "week-2 integration gate" without "vertical-slice" | `source/gdd.md` §4.7 open-questions table, Q20 |
| §4.10's claim that §2.11 specifies no save/load surface still holds | `source/gdd.md` §2.11.5: "That is the complete screen list for the prototype: title/menu, briefing, match, result." |
| "addendum Part A" names a real, cited artifact | `source/gdd.md` §3 ledger paragraph: "authored from `spec/combat_spec.md` (+ `combat_spec_addendum.md`) … 17/17 on a live `g++`/`clang++` compile+run", commit `5ffa8d6` |
| T-SCN-08's fixture numbers come from §2.13.1, not from me | `source/gdd.md` §2.13.1 lane table, *Longwater March* row: west 3 MP, east 4 MP; and its closing paragraph naming the same 3/4 split as the odd-r argument |
| Nothing else in §4 is built | `source/gdd.md` §3 ledger: Hex grid, movement, capture, Fame, turn loop, AI, data tables and UI all `*pending*`; four rows green at `5ffa8d6` |
