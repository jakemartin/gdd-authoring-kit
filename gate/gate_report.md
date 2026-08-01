# Continuity gate — run `rubric-round-2d`

**Top-level verdict: PASS — 0 violations across four sections.**

`source/MANIFEST.txt` present. `source/gdd.md` md5 `3b9024f384162b32959416b66f5f1137`;
`source/kb_rules.md` md5 `e99ae4ec2c63dcadd6b5e5d5a66067bd`; `source/kb_setting.md`
md5 `b3e9e89daaef1cdeb333e3fb4368d1c0` — all three unchanged from `rubric-round-2b`
and `-2c`, so nothing beneath any of the four files has moved.

Four files in scope, **19 replacement pairs** (tech 11, rules 2, scenario 3, ux 3).
No OLD or NEW block changed this pass. `scenario_rubric-round-2.md` is the only
file that moved at all, and only on its reporting surfaces. The three prior PASS
verdicts are re-recorded, not re-litigated; the whole of this pass is the one
clause `rubric-round-2c` blocked on, plus the self-sweep the author volunteered
alongside it.

---

## The filed violation — closed on the merits

`rubric-round-2c` filed one `dead-reference`: the zero-citation row asserted
"**§4.11's row-7 and row-10 paragraphs cite §2.13.5 and §4.10, never §2.13.6**"
in a document where §4.11 carries no `2.13` at any depth. The author **deleted**
the positive half rather than repairing it. The row now reads:

> **§2.8** and **§4.11**. Both were named as citing sites in my round-1 filing;
> neither contains the string. §4.11 (lines 2526–2578) contains no occurrence of
> `2.13` at all. **Q16 does not cite it either** — its Blocks cell reads *"All
> three §2.13 maps; the terrain schema"*.

Verified independently, not from the author's report:

- **The negative is exact.** A document-wide sweep for `2.13` in any form returns
  **116 hits, last at line 2301**. §4.11 opens at line **2526** (`### 4.11 Build
  order`) and runs to the end of the document at **2578**. Zero occurrences in
  range — a strictly stronger statement than "cites §2.13.6 zero times", and the
  one the gate named as the correct form of the point.
- **Nothing positive is asserted about §4.11's citations.** The clause naming
  what §4.11 cites instead is gone. What remains is the negative plus one piece
  of evidence *for* the negative: Q16's Blocks cell, quoted verbatim. Source line
  **2287**: `| **Q16** | Recon/Air vs. Water. … | All three §2.13 maps; the
  terrain schema | Recon is a **land** unit …` — character-for-character match,
  and the cell visibly carries `§2.13` without the `.6`, which is exactly the
  distinction under test.
- **Grammar and sufficiency.** The row is a complete four-sentence unit; the
  deletion left no fragment. It states everything the finding it supports needs
  — Pair 3 strands nothing in §2.8, §4.11 or Q16 — and states more than the
  round-2c version did, since "no `2.13` at all" subsumes "no `2.13.6`".

For completeness on the facts the round-2c filing turned on, both re-derived
this pass: §4.11's row-7 paragraph's only §2 citation is **§2.11.6 at line
2568**; `§4.10` occurs inside §4.11 only at lines **2529**, **2532** and in the
row-10 table cell at **2550**, never inside the row-7 paragraph (2552–2569) or
the row-10 paragraph (2570–2577). The author's account of both agrees with mine.

## The volunteered self-sweep — both line numbers check

The author swept its own file for the same defect class, found one sibling in
the `tech-director` handoff, and instead of deleting it **located the strings
and attached line numbers**. This is the class that has failed three times in
this file, so both were verified against source character by character.

| Claim as filed | Source, at the line given | Ruling |
|---|---|---|
| *"row 7's **structural** half for the `scenarioId`/`scenarioHash` it loads"* — **(line 2550)**, attributed to §4.11 **row 10(b)** | Line 2550, row 10's Depends-on cell, part (b): "(b) *Headless replayer* — rows 1–3, plus row 7's **structural** half for the `scenarioId`/`scenarioHash` it loads; it runs T-SAVE-01/02/03/05/06 over week 2's `{Move, Attack}` log." | **Exact.** Quote verbatim, line correct, and the sub-part attribution `10(b)` is correct — it is part (b) of that cell, not (a) or (c). |
| *"Row 7 is still not ON the critical path (nothing in the chain waits on it)"* — **(lines 2565–2566)** | Line 2565 ends `… and not merely agree with the repo. Row 7 is`; line 2566 opens `still not ON the critical path (nothing in the chain waits on it), but` | **Exact.** The sentence soft-wraps across exactly those two lines; the range is right and the quote is verbatim across the wrap. |

The two supporting claims attached to them also hold: §4.10's save header does
carry both fields (line **2470**, `| `scenarioId` / `scenarioHash` | string |
The §4.7 Stub-7 scenario file and its hash |`, inside §4.10 which opens at line
**2447**), and row 7's ledger row is scheduled to flip after movement — source
line 2569, "the scenario row flips after movement, not before," with row 3 being
Movement & pathfinding in the same table.

**Same claims, or new assertions?** The two line numbers appear in three places
— the two collision-report bullets, the `tech-director` handoff, and the
Grounding row "Stub 7 is core-side". All three carry the **same two claims** with
the **same two loci**; no new assertion is introduced by the repetition, and no
locus contradicts another. The Grounding row is the compressed index form of the
collision bullets, pointing at the same evidence.

**Two things examined and deliberately not filed**, recorded so the ruling is
auditable:

- The Grounding row labels lines 2565–2566 "the row-7 paragraph". That paragraph
  actually runs 2552–2569. The line numbers locate the load-bearing *sentence*
  inside it, which is what the citation is for, and the collision bullet attaches
  the identical numbers unambiguously to the quoted string. A reader following
  2565–2566 lands on exactly the text the claim rests on. Same ruling as the
  1249/1250 wrap cleared at `rubric-round-2c`: the conclusion under test is exact
  at the line given. Not a defect.
- The summary says "every positive claim left in the file carries the line number
  it was verified at." Read as a universal over the whole file that is
  overstated — §4.4's wk-2 and wk-4 quotes, §2.13.2's `turnCap` and §4.10's save
  header are cited by section, not by line. Read in its own context — positive
  claims *of the class just discussed*, i.e. positives volunteered in support of
  a negative finding — it is true, and I checked every such site in the file to
  confirm it: the zero-citation row, Pair 3's note and the Grounding sweep row
  are now purely negative, and the handoff's two positives serve a different
  proposition and both carry line numbers. This is a claim about the draft's own
  presentation, not about `source/gdd.md`; no reading of it leaves the Director
  holding a false fact about the master document. Loose universal, same class as
  the Pair 2 metonymy cleared last round. Not filed.

## Everything else, re-confirmed rather than re-litigated

Per the brief, the cleared material was checked only for invalidation by the
prose edit, and none of it moved:

- **The pairs.** All three OLD blocks re-matched against source this pass and
  each occurs exactly once: Pair 1 at lines **1305–1306** (§2.13.7's closing cut
  line, verbatim), Pair 2 at **1114–1115** with row 7–8 reproduced unchanged as
  the anchor (verbatim), Pair 3 at **1203**. Pair 2's NEW cell `Stretch P2 (wk
  4)` is still character-for-character §2.13.7's Status cell at line **1303**.
- **The §2.13.6 sweep.** Unchanged text, and its figures still agree with the
  independent derivation recorded at `rubric-round-2c`: 12 occurrences on 11
  lines, 11 citations on 10, split 1 to §2.13.2 (line 1073) and 10 to §4.7, Q17
  counted twice at line 2288, §2.8 / §4.11 / Q16 at zero.
- **Placement collisions.** Nineteen pairs, nineteen non-overlapping sites. The
  prose edit touches no placement. No collision within `scenario_` or against
  `tech_`, `rules_`, `ux_`.
- **kb-desync.** Both KB files unchanged at the same md5s and carrying no match
  for `stretch`, `Causeway` or `Longwater`. Nothing this round makes either wrong.
- **Voice and format.** Declarative present tense throughout the rewritten
  passage; no UI string authored. All required headings still present in
  `scenario_` (Placement, the pairs surface, Change requests, Open questions for
  the Director, Grounding).

---

## `sections/tech_rubric-round-2.md` — **PASS**, 0 violations

Byte-unchanged. Checked only for invalidation: `scenario_`'s corrected handoff
now asserts nothing about what §4.11 cites, and `tech_` never claimed §4.11 cites
§2.13.6, so the correction disturbs nothing on the tech side. `tech_`'s two
§2.13.6 citations remain the bare label form Pair 3 preserves — "(a) *The
Causeway* §2.13.6 (Stretch P2)" and "*The Causeway* §2.13.6 (Stretch P2)". The
PASS stands for the third consecutive run.

## `sections/rules_rubric-round-2.md` — **PASS**, 0 violations

Byte-unchanged. Its two closures depend on §2.13.7's Status cells (lines
1302–1303) and Q13's in-force reading, none of which the prose edit touches. The
PASS stands, and the co-merge requirement stands with it.

## `sections/ux_rubric-round-2.md` — **PASS**, 0 violations

Byte-unchanged, passed at all four runs. It places nothing in §2.13 and cites
§2.13.6 nowhere. The PASS stands.

## `sections/scenario_rubric-round-2.md` — **PASS**, 0 violations

Fourth pass, and the first clean one. The three pairs have been correct
throughout and are correct now; every round since `rubric-round-2b` has been
about the accuracy of the file's own verification prose, and that is now exact.
The blocked clause is gone rather than reworded, the negative it was run to
establish is stated in its strongest true form, and the one sibling the author
found in its own sweep is not merely asserted but pinned to two line numbers
that both hold on inspection. No OLD or NEW block changed; nothing downstream
needs to move.

---

## Verdict

**PASS**, on all four files, with zero violations in any of them.
`tech_rubric-round-2.md`, `rules_rubric-round-2.md` and `ux_rubric-round-2.md`
are byte-unchanged and could not be invalidated by an edit confined to
`scenario_`'s reporting prose inside §2.13 — I confirmed the one surface where
they touch, `scenario_`'s `tech-director` handoff, and it now asserts nothing
`tech_` contradicts. `scenario_rubric-round-2.md` closes its last violation by
deletion rather than repair, which is the right instrument: the zero-citation row
now states only the negative, and states it as "§4.11, lines 2526–2578, contains
no occurrence of `2.13` at all", which I verified against a document-wide sweep
whose last `2.13` hit is line 2301. The self-sweep it volunteered is the part
that could have introduced a fourth error and did not — both quoted strings
appear verbatim at the lines given, row 10(b)'s dependency text at line 2550 and
the row-7 critical-path sentence wrapping across 2565–2566, and the same two
claims carry the same two loci in all three places they appear. Nothing must
happen before merge on the gate's account: the round is mergeable as it stands,
in one commit, with `rules_`'s §2.10 pair and `scenario_`'s Pairs 1–3 landing
together or not at all, since Pair 1's exclusivity sentence is false if the §2.10
edit does not land with it. Two items remain in the Director's hands and are not
gate findings: the §4.7 Stub-7 scope question flagged in `scenario_`'s collision
report, and the cosmetic `§4.4 wk 4` / `wk 4` asymmetry between §2.13.5's and
§2.13.6's headers.
