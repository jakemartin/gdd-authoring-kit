# Gate report — run `deletion-recorded-3`

`source/MANIFEST.txt` present. `gdd.md` md5 `8c738e860a403d254af0317533b23c75`,
matching the md5 the draft states it copied its OLD strings from, and matching
the md5 recorded in the run-2 accept record.

Sections produced by this stage: one — `sections/tech_deletion-recorded.md`.
Placement collisions are only visible in the aggregate; the aggregate here is a
single file targeting §3's evidence prose, so no collision exists.

**How the master was measured, and where.** `source/gdd.md` is hard-wrapped and
§3's evidence prose is a single line — every §3 string checked below returned
**line 1516**, from `Stale claims in the crew repo were repaired at …` through
`Legend: **Author** ∈ {agent,`, which confirms the single-line property the
draft relies on. Because a line-oriented sweep suppresses that line, every check
below was run newline-insensitively (`multiline`) with match-only (`-o`) output
and windows kept short. Each finding, clearance and locator in this report names
the line the measurement was taken on. I did not independently count the
characters of line 1516; the `~44 000` figure in the draft's sweep note is
descriptive and nothing in the draft depends on its exact value.

---

## `sections/tech_deletion-recorded.md` — **PASS** (0 violations)

Nothing is filed. What follows is the record of what was measured, so the
clearance is auditable rather than asserted.

### 1. The run-2 violation, re-measured

The run-2 finding was that row 10's candidate column filed a disposition against
`§3 ledger table \`Evidence\` cells citing \`9289c1d\``, which do not exist.

Row 10 now reads:

> | 10 | §3 `Both are green at [`9289c1d`] over the vendored tree at `0897cb5`` | **Left** | A green attribution is about runs. No vendored byte moved at `b5f524d`. |

The false locator is gone. The sentence it now names is real and unique:
`Both are green at [\`9289c1d\`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d) over the vendored tree at \`0897cb5\`, where the …`
occurs **once**, on **line 1516**, measured whole-file and newline-insensitively.
No other occurrence of `Both are green at` exists in the file.

The disposition (**Left**) and the reason are unchanged from the version I
verified at run 2 — I hold run 2's verbatim copy of that row in
`gate/accept.json`'s `draft_quote`, and the only difference is the reworded
subject the author reports (`Green attributions are…` → `A green attribution
is…`), which the singular subject now requires. The reason is true: `9289c1d`'s
greens are run attributions over the vendored tree at `0897cb5`, and the fact
block's §2.5 establishes that none of `b5f524d`'s ten files is a vendored module
source or in the UE project repo at all.

**Measured and not filed.** The quoted candidate elides the markdown link target
between `]` and ` over`; the literal string as printed occurs **0** times, and
the same string with the URL restored occurs **1** time, on line 1516. The
grounding row's claim — the sentence occurs once, in §3's evidence prose at line
1516 — is true of the sentence it names, the elision drops no word of master
prose, and the candidate is uniquely identifiable. Note for future rounds only:
rows 5 and 9 mark the same elision with `…`, and row 10 does not.

### 2. The unfiled conversion of the candidate column — tested, not accepted

The author converted the whole column to quoted-master-text-plus-section-number
and collapsed two further sub-section locators. Both collapses were tested
against the claim that this is claim-surface removal only.

- **Row 11**, now `§4.5 \`… among what its closure waits on is a further editor
  pass replaying the widened fixture in-engine, none having run since
  \`0897cb5\` (§3)\``. That text occurs on **line 1589**, which is inside §4.5
  (heading at line 1579, section ends line 1590). The collapsed locator "risk
  row" was accurate — line 1589 is the risk-table row — so nothing false was
  removed and nothing false was introduced. Disposition **Left**, reason
  unchanged in substance and true: the sentence is about runs, not clause text,
  and remains true after `b5f524d`.
- **Row 15**, now `§1.7, all of it`. §1.7 exists (heading line 74, running to
  line 102). Its reason is verifiable and verified: I read lines 74–102 in full;
  `9289c1d`, `b5f524d` and the fourteen clauses appear nowhere in them, and the
  section's change table has exactly rows 1–5, so the collapsed locator was also
  accurate. The candidate is still identifiable — a named section read in its
  entirety is a wider target than a quote, not a vaguer one.
- **No candidate has become unidentifiable.** Every other row carries quoted
  master text that resolves to exactly one place: row 1, row 2, row 3 (the two
  OLDs and the interstitial sentence, all line 1516), row 4 (line 1516,
  immediately upstream of OLD 1), row 5 (line 1516; the quote carries `9289c1d`,
  which distinguishes it from the second `Stale claims in the crew repo were
  repaired at [\`c2edae0\`]` sentence on the same line), rows 6–9 (line 1516),
  row 12 (line 1589, §4.5), row 13 (§4.9, lines 2968–2969), row 14 (line 3253,
  §4.11), row 16 (line 1516).
- **No disposition or reason moved.** Every row's disposition is **Left** except
  rows 1 and 3 (**Edited**), row 2 (**Left, verbatim**), rows 4 and 7 (**Left,
  filed**) and row 16 (**Left; restated…**) — the same set as run 2, and each
  reason was re-checked against the master on the merits rather than against
  memory. None depends on a locator that was removed.

### 3. Re-checked from runs 1 and 2, not assumed to have survived

- **Both OLDs byte-exact and unique.** OLD 1 returns **1** match; OLD 2 returns
  **1** match. Stronger: the three-sentence span
  `**That same commit introduced false claims of its own:** … the true negative
  stands.` — OLD 1, then the interstitial sentence, then OLD 2 — matches as one
  contiguous string exactly **once**, on line 1516. That single measurement
  proves byte-exactness, uniqueness, adjacency and ordering at the same time.
- **The untouched interstitial sentence.** `They ran and passed and did not
  close, so all fourteen are false.` sits between the two OLDs in that same
  contiguous match, is quoted unedited in the draft, and is untouched by both
  pairs. The paragraph stays coherent across the replacement: Pair 2's NEW opens
  in the past tense (`such a clause sat beside a true negative`), so the
  present-tense falsity sentence upstream is not contradicted, and the NEW's own
  `so all fourteen remain false` restates it after the deletion record rather
  than replacing it. The master text following OLD 2 (`**Two commit messages
  carry claims measurement contradicts…`, line 1516) is undisturbed.
- **Fact-block §4 error species, against both NEWs.** 1 — every finite claim
  about crew-tree contents in Pair 2's NEW is enclosed by a clause naming
  `b5f524d` (`were deleted at b5f524d`, `kept as written there`, `deleted with
  the closure clause`, `none of the ten files it touched`); the surviving
  present-tense verbs are `remain false` (a property of propositions), `remain
  open` (a property of acceptance IDs, corroborated at §4.5 line 1589) and
  `records a deletion` (a property of the commit). 2 — `has since` appears in
  neither NEW. 3 — falsity is not weakened: `all fourteen remain false` is
  present tense, `what ended at b5f524d is their presence in the crew repo and
  nothing else` names which half ended, and the interstitial sentence is
  untouched. 4 — `**All fourteen were deleted**`, `across those same ten files`,
  with a per-file distribution; no narrowing quantifier. 5 — three dispositions
  present and named, matching fact block §2.4 and appendix §A site for site.
- **Every count.** `71`, `62`, `9`, row 9's unclosed `3` and row 10's `1` all
  appear verbatim at §4.5 line 1589 and at §3 line 1516's most recent landing
  sentence (row 16's quote, confirmed verbatim). The per-file distribution
  3 + 2 + 2 + 7 × 1 = **14** across 1 + 1 + 1 + 7 = **10** reconciles exactly
  with fact block §2.2, and the seven single-clause files the draft names are
  the seven that carry 1 there. `10-file, +26 / −31` matches §2.1. The Build
  order table moves nothing and says so.
- **Referents a master-only reader must resolve.** `the bridge landing at UE
  \`0897cb5\`` resolves: line 1516 carries `part 2's bridge landed, at
  \`0897cb5\` in the Stratocracy UE project repo`, restated at lines 2945–2946.
  `the crew repo` is the master's own phrase (line 1516, twice). The no-closure
  substance is the master's own sentence, `\`T-INT-02\`, \`T-INT-03\` and
  \`T-SAVE-06\` ran and passed, and none of them closes.**` (line 1516), with
  §4.9 (line 2968) and §4.4 (line 1577) restating it. `b5f524d`, `CR-1` and
  `parity_fixture` each occur **0** times in `source/gdd.md` — measured over the
  whole of `source/`, where they appear only in the fact blocks — so the NEW
  introduces `b5f524d` and leans on neither of the other two.
- **The `14` collision the draft flags.** Real and correctly characterised: line
  1516's `This commit **modifies only** — … 14 files changed: \`README.md\`,
  \`crew/tools.py\`, …` belongs to the commit whose subject is, on the same
  line, `T-TURN-01's move/act split into two independent per-unit flags, the new
  \`T-TURN-10\` build allowance, and T-FAME-04's dropped per-turn clause`. Pair
  2's NEW writes `10-file` and never `14 files`.
- **The "three sentences upstream" claim** in the sweep note is true measured to
  Pair 2's OLD: on line 1516 the `Sentences of the form *"they do not run
  **here**"*…` sentence is followed by OLD 1, the interstitial sentence, then
  OLD 2.
- **Format, voice, scope, kb.** All five required headings present — Placement,
  Draft, Change requests, Open questions, Grounding. Voice matches §3's
  declarative ledger register. No scope breach: §3's provenance ledger is the
  tech-director's lane, and no ledger row, count, acceptance ID or open-question
  row moves. No `kb-desync`: `kb_rules.md` contains **0** occurrences of
  `9289c1d`, `T-SAVE-06` or `fourteen`, and both pairs land in §3, not §2. No
  `unverified-claim`: the draft restates no gate figure for `b5f524d` and says
  so in the NEW itself. Open question 7 is new and additive; 1–6 are unchanged
  in substance and each remains a live question rather than a claim.

---

## Verdict

**PASS.** The run-2 violation is repaired at its root rather than papered over:
row 10 no longer asserts a location inside §3 and now carries master text that
resolves to one place, line 1516, with its disposition and reason intact. The
unfiled conversion of the whole candidate column was tested rather than
accepted — every disposition and reason is the one I verified at run 2, no
candidate lost identifiability, and the two collapsed locators (rows 11 and 15)
were themselves accurate before collapse, so the change removed claim surface
without removing truth. Everything cleared at runs 1 and 2 was re-measured
rather than carried: both OLDs are byte-exact and unique and, together with the
untouched `They ran and passed and did not close, so all fourteen are false.`,
match as a single contiguous span exactly once on line 1516; no fact-block §4
error species is committed by either NEW; and every count reconciles with §4.5
line 1589 and fact block §2.1–§2.5. Nothing must happen before merge beyond the
Director's own checklist — apply both pairs at §3's evidence prose, rebuild the
`.pdf`/`.txt`, re-sync `kb/rules.md` (unaffected here, since neither pair
touches §2), and re-run `python sync.py`; the seven open questions are for the
Director's ruling and none of them blocks this file.
