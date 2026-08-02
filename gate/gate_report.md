# Continuity gate — run `post-merge-22`

**Artifact under test:** `source/gdd.md`, the merged master, md5
`d3f6913b1ecf228c19811328db33b27d` (pre-merge `3b9024f384162b32959416b66f5f1137`).
`source/MANIFEST.txt` present; the md5 above is taken from its `gdd.md` line.
`source/kb_rules.md` md5 `e99ae4ec2c63dcadd6b5e5d5a66067bd` and
`source/kb_setting.md` md5 `b3e9e89daaef1cdeb333e3fb4368d1c0`, both byte-unchanged
from before the merge.

**Top-level verdict: PASS. Zero violations across twelve checked areas.**

This is a post-merge run: the object is the merged document, not the drafts. The
four `*_rubric-round-2.md` addenda were read only to recover what each pair was
*intended* to do, never as the object of the gate.

---

## Landing check — all 19 pairs

Nineteen OLD/NEW pairs were declared: tech 11 (Pairs 1, 2, 3, 4–8, 9, 10, 11),
scenario 3, ux 3, rules 2. All nineteen are present in the merged document, at
the placement each pair specified, and every NEW block matches its addendum
character-for-character where I compared them (§2.10, §2.13.7, §2.13.4, §2.13.6,
§1.7, §4.11's legend, §3's role rows and placing note).

No pair landed twice and none landed partially. Seven phrases unique to a
replacement seam — `Claude Code is the agent client`, `Reading this table`,
`The stretch condition`, `Beneath the tier`, `The cut line`, `Critical path:`,
`Status: live tracker` — return exactly seven matches between them, i.e. one
each. No duplicated sentence, orphaned fragment or broken table row was found at
any seam.

Heading nesting is intact. §1.7 sits at `##`, matching §1.5 and §1.6, between
§1.6's table and the `---` divider that precedes `## 2. Game Mechanics`. The
full heading list runs 1 → 1.5 → 1.6 → 1.7 → 2 → 2.0…2.13.7 → 3 → 4 → 4.1…4.11
with no gap, no duplicate and no level error.

---

## §1.7 — new subsection

Every claim in the five-row table was checked against the register row it
summarises.

- Row 1 (Q8): the four §2.7 sites, §2.9's economy phase, T-FAME-02/04 and the
  two `kb/rules.md` lines match Q8's own cell verbatim. The two sentences §1.7
  quotes as the *finding* — "both players have income from turn 1" and "plus
  home-factory income from turn 1" — are correctly absent from the merged §2.7,
  which now reads "both players draw income from **turn 2**, the first accrual".
  §2.13.2's "100 of the 200 starting Fame" is present as quoted.
- Row 2 (Q23, Q20): critical path `1 → 3 → 4 → 5 → 6/8`, the week-3 slice, the
  week-2 format, the amendment, "the third disagreement", and the Q29
  registration all match §4.4, §4.11 and the Q20/Q23 cells.
- Row 3 (Q22, Q28): "five of six lanes clear and one exact tie", (9,5) → (9,1),
  "5 against 6 in both seats", fixture (b), and "the register now states that
  limit once" all match Q22, Q28, §2.13.2 and the register preamble.
- Row 4 (Q6): the six uncited sites are enumerated with the same grouping Q6
  uses (§2.11's standings row and its tooltip counted as one), giving four
  in-document plus two in `kb/rules.md`. All six were located and confirmed
  corrected.
- Row 5 (§4.6): re-derived independently. $0.69, $1.725, $1.035, 210 × $0.69 =
  $144.90, 32 × $1.035 = $33.12, subtotal $178.02, 315 × $0.69 + 47 × $1.035 =
  $265.995 ≈ $266, $266 + $37 = $303, and the stated $1.005 gap to the retired
  $267. Every figure holds.

§1.7 **restates no register count or extent**, as instructed. It says only
"§4.7's register is the authoritative record of which rows exist and what each
was ruled; the five entries below are the ones that changed the *game* or its
evidence" — a count of its own rows, not of the register. It therefore does not
collide with §4.7's rule that "the register below is the single place their
extent is stated".

§1.5, §1.6 and §1.7 read as one non-overlapping history: First → Final, Final →
Production, Production → the ruling cycle. §1.7's opening ("the crew was
forbidden to invent one and filed it instead as a numbered open question in
§4.7's register") matches §1.6 row 4's "where a rule was missing, it is filed as
a numbered open question in §4.7's register instead of being invented." Nothing
in the document cites §1 content by position, so §1.7's insertion breaks no
reference; `§1.5 #1`, `§1.5 #5` and `§1.6 row 5` all still resolve to the rows
they name.

## §2.10 against §2.13.7, §4.4 and §4.11 — the round's decisive settlement

**The condition is stated in §2.13.7 alone.** A document-wide sweep for the
ordering clause returns one hit: line 1361, inside §2.13.7. Every other site
that names the set carries labels only — §2.10's STRETCH row (`P1, wk 4` /
`P2, wk 4` plus an explicit pointer, "shipping under the conditions §2.13.7
states, which that section states alone"), §2.13.4's ladder rows, §2.13.5's and
§2.13.6's headers, and §2.13.7's own summary table. §2.13.7's "four clauses"
count is exact: no forward pull, no blocking core, *The Causeway* only after
*Longwater March*, and the week-4 balance condition.

§4.11's cut-line bullet quotes "the set stays on paper" **with attribution to
§2.13.7** rather than restating the condition in its own words, which is the
behaviour §2.13.7 asks for and produces no second owner.

**§2.10's placements agree with what §4.4 and §4.11 schedule.** Checked one by
one: guided opening wk 5 = §4.4's "onboarding"; §4.10 format + headless replayer
wk 2 = §4.4 wk 2 and §4.11 row 10(a)/(b); minimal single-slot save/load wk 5 =
§4.4's "save-slot UI and its slot I/O"; capture + Fame production wk 3 = §4.4
wk 3 and rows 4–5; scenario file + headless validator = §4.4 wk 2's "loading,
validating and rendering" and §4.11 row 7. The IN/STRETCH split of the MCP
toolset (wrapper stretch, wrapped validator core) matches §4.11 row 7's
"MCP tool wraps it in-editor, manual fallback stands" and Stub 7's closing note.

The four "Reading this table" bullets each check out against their cited source:
§1's *Scope at a glance* and §4.5's MVP line; §4.4's stated rule *a format is a
test instrument; slot I/O is a feature*; §4.11's row-7 and row-8 dependency
cells, §2.8's `turnCap` and §2.11.6's `guidedOpening`; and §2.13.7's ownership of
the stretch condition.

## §3 and §4.5 — the four re-derived figures

All four were recomputed from the merged document rather than accepted.

- **4 verified ledger rows.** Combat resolution, Test suite, Repair,
  Type-effectiveness carry ✓. All four cite `Combat.cpp` / `test_combat.cpp`
  @ `5ffa8d6`, so §4.5's "all four inside Combat" holds.
- **8 `*pending*` rows.** Hex grid, Movement, Capture & Fame, Turn loop,
  Opponent AI, Data tables, Content/scenario, UI.
- **69 written acceptance IDs (§4.7–§4.11).** Counted from the ten acceptance
  sets: T-HEX 7 + T-DATA 6 + T-MOVE 6 + T-FAME 9 + T-TURN 9 + T-AI 6 + T-SCN 10
  + T-UI 4 + T-INT 5 + T-SAVE 7 = 69. T-MOVE-07 and T-SCN-10 are correctly
  excluded as reserved-and-unwritten; T-COMBAT, T-REPAIR and T-CAP are correctly
  excluded as living outside §4.7–§4.11.
- **Week 1 due rows 1–3, unmet at 2026-08-01.** §4.4 week 1 names §4.11 rows 1–3
  (grid and hex math, the §4.8 tables, movement and pathfinding); all three read
  `*pending*` in the §3 table. The "three days past the last code commit" line is
  consistent with the Director-supplied 2026-07-29 gate-verification date.

§3's claim that only row 2, row 10(a)'s format spec, T-INT-01/04 and the
parallel UMG skeletons proceed meanwhile is correct against §4.11: row 2 "runs
in parallel immediately", row 10(a) has "no deps at all", T-INT-01/04 "depend on
no rules row at all", and §4.4 week 1 starts the UMG skeletons in parallel.
Everything else in §4.11 traces back through rows 1–3.

§4.5's risk row states **no count** of the cut line and defers to §4.11's table
as authoritative, matching §4.7's head note. No site in the document pins a †
count, so nothing can go stale there.

## §4.11's cut line and its legend

Nine IDs carry †: T-DATA-05 (row 2); T-SCN-08, 09, 11 (row 7); T-UI-03, 04
(row 8); T-INT-02, 05 (row 9); T-SAVE-06 (row 10). The legend's five bullets
partition exactly those nine and additionally explain why T-SAVE-07 is unmarked.
The † glyph appears nowhere else in the document, so it collides with no other
footnote convention.

The legend's supporting facts check out: T-DATA-05's fallback tables are 4 unit
rows × 11 columns and 7 terrain rows × 10 columns, both counts correct against
§4.8; T-SCN-08's fixtures (a)/(b) are the two stretch maps and (c) the synthetic
refusal; T-SCN-11 keeps its two shipped-map fixtures including the failing one;
T-SCN-09's asserting branch is stretch-only because the shipped map declares
`none`; T-UI-01/02 are headless and 03/04 in-editor per Stub 8's acceptance
line; T-INT-01/04 run on every gate run per §4.9's acceptance line; T-INT-03 is
correctly held unmarked on the rule that no marked ID may guard a rules
invariant, against §4.9's "an invalid command returns a rejection reason and
changes nothing". T-SAVE-07's unmarked status is consistent with §2.13.7's slip
condition, under which self-play still runs.

Nothing in the legend contradicts §4.4, §2.13.7 or §4.9 about what runs when.
§4.4's week-2/week-3 run-versus-close split matches §4.11 rows 9 and 10 exactly,
including which IDs close in which week.

## §2.11.6's re-derived Fame guarantee, in its merged surroundings

Beat 3's constraint holds against the two sections this merge did not touch.
§2.9 gives Easy = player +150, Normal = even 200/200, Hard = player −100; §2.7
converts those to a player opening of 350 / 200 / 100 with the AI on 200 at
every tier. §2.11.6's default is Easy, so 350; the floor across pickable tiers is
Hard's 100, which is not below Infantry's 100. "Builds are Fame's only sink" is
correct — repair is free and capture costs nothing. The guarantee that an
outstanding beat 3 means nothing has been spent depends on spend implying spawn,
which holds for the player because §2.11.5 disables Build while a factory is
boxed in (Q31), so queue time and spawn time are the same instant. The
no-turn-1-income clause matches §2.7's Q8 ruling.

## Cross-reference sweep after the structural edits

- The §2.13.6 heading change broke nothing: every citation of §2.13.6 in the
  document (§2.13.2, §2.13.1, Stub 7's T-SCN-09 and asymmetry (ii), Q17,
  §2.13.7, §4.11's legend) refers to the section by number or quotes its body,
  never its heading text.
- No pointer into §2.10's old table shape survives. Q1's "§2.2 and §2.10 never
  state the prototype map's size or shape", Q13's "§2.10 does not scope one",
  Q23's quotation of "these land wk 3, not wk 1–2", §4.4's quotation of the same
  string, and the §2.10-IN citations in §2.13.2 and §2.13.7 all still resolve
  against the new table.
- §1.7's insertion shifted no reference: nothing in the document cites §1 by
  position.
- All new cross-references resolve: §4.5 → §4.7 head and §4.11's table; §4.7
  head → §4.5's MVP line and §2.13.7's stretch maps; §4.11's legend → §4.7 head;
  §2.10's note → §1, §4.4, §4.5, §4.11 rows 7, 8 and 10, §2.8, §2.11.6, §2.13.7;
  §2.11.4 and §2.11.6 → `kb/setting.md`.

## Record: `kb/rules.md` needed no re-sync — confirmed, both halves independently

**Half one — what `kb_rules.md` parses.** Read in full. Its four content blocks
are Units (§2.4), Terrain (§2.3), Economy — Fame (§2.7, with the §2.9 handicap),
and Victory & outcomes (§2.8, with §2.13.2's turn cap). Nothing in the file
derives from §2.10, §2.11, §2.13.4/.6/.7, §3, §4.5, §4.7 or §4.11. The header's
own claim — "§2.3 terrain, §2.4 units, §2.7 economy, §2.8 victory" — is accurate
to the file's contents.

**Half two — what this merge touched.** The nineteen pairs land in §1.7, §2.10,
§2.11.4, §2.11.6, §2.13.4, §2.13.6, §2.13.7, §3, §4.5, §4.7 and §4.11, and
nowhere else. None of §2.3, §2.4, §2.7 or §2.8 was opened. §2.9 and §2.13.2,
which `kb_rules.md` also draws two figures from, were likewise untouched.

Both halves hold, so `kb/rules.md` is not stale and the downstream critic is not
validating against dead rules. No `kb-desync` violation is filed.

`kb_setting.md` was also checked, because §2.11.4 and §2.11.6 now cite it by
name. Every constraint they attribute to it is present in it verbatim: the
≤ 30-word result line and ≤ 40-word codex blurb, "Faction voice appears only in
result-screen text", the terse-tactical-briefing register, substance over drama,
the banned-register list, the two faction voice blocks as characterised, and the
pipeline note that retrieves a faction block only for result-screen content.
§2.11.6's statement that one-shot tips "are not a length category it names" is
correct — the file names two length categories and neither is a one-shot tip.
Neither citation asserts anything the file does not say, so `kb/setting.md`
needs no re-sync either.

---

## Verdict

**PASS.** All nineteen replacements are in place, in the right sections, whole
and unduplicated; the merged document holds together across the interactions the
draft-by-draft round could not see. The round's decisive settlement survived the
merge intact — the stretch condition is stated in §2.13.7 and only there, every
other site carries labels and a pointer, and §2.10's IN/STRETCH placement agrees
item for item with what §4.4 and §4.11 schedule. The four figures §3 and §4.5
assert about the build's position were re-derived from the merged document rather
than accepted: 4 verified rows, 8 `*pending*`, 69 written acceptance IDs, and
week 1's rows 1–3 unmet at 2026-08-01 all hold, and the 69 in particular sums
exactly across the ten acceptance sets. The nine † marks are partitioned
completely by their legend and contradict nothing about what runs when.
`kb/rules.md` needed no re-sync, and both halves of that claim were verified
independently rather than one inferred from the other. Nothing must happen before
merge, because the merge has already happened and it is clean; this record exists
to say so. The one item still owed to the Director is unchanged and unrelated to
this run: the title / lineage framing remains unowned, awaiting a Tier-2
`narrative-designer`.
