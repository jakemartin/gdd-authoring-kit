# Continuity gate — run `post-merge-11`

**Audit target:** `source/gdd.md`, md5 `68991030a238c1804a3234db2fa0485f`
(manifest line: `gdd.md <- E:\MultiAgent\stratocracy-content\Stratocracy_Prototype_GDD.md`),
plus `source/kb_rules.md` (`0c1884f9e06619b35ae7608c824e8b93`) and
`source/kb_setting.md` (`b3e9e89daaef1cdeb333e3fb4368d1c0`).
`source/MANIFEST.txt` is present — the run proceeds.

**Top-level verdict: PASS. Zero violations.**

**Scope note.** `sections/` holds 20 files. One — `sections/tech_post-merge-11.md`
— is this stage's draft, now applied and sealed under the `✅ APPLIED ADDENDUM`
header. The other 19 are superseded drafts and sealed addenda. Only one draft
targets the master this run, so there is no placement to collide with; all four
replacement pairs were compared against the merged text and all four are applied
verbatim. Re-audited in full; nothing carried forward from `post-merge-10`.

---

## Per-area verdicts

| Area | Verdict | Violations |
|---|---|---|
| §1, §1.5, §1.6 | **PASS** | 0 |
| §2.0–§2.10 | **PASS** | 0 |
| §2.11 (UI/UX + onboarding, incl. §2.11.6-B beat schedule) | **PASS** | 0 |
| §2.12–§2.13.1 (lineage, layout conventions, opening-capture invariant, symmetry facts) | **PASS** | 0 |
| §2.13.2–§2.13.7 (*Ferrum Crossing*, eight-route table, stretch maps, summary) | **PASS** | 0 |
| §3 (AI architecture + provenance ledger) | **PASS** | 0 |
| §4.1–§4.3, §4.5, §4.6, §4.8–§4.10 | **PASS** | 0 |
| §4.4 + §4.11 (the schedule seam) | **PASS** | 0 |
| §4.7 Stub 7 — the four repaired sites | **PASS** | 0 |
| §4.7 register Q1–Q29 (incl. Q17) | **PASS** | 0 |
| `source/kb_rules.md` | **PASS** | 0 |
| `source/kb_setting.md` | **PASS** | 0 |
| `sections/tech_post-merge-11.md` (draft, sealed) | **PASS** | 0 |
| `sections/` — remaining 19 files | **PASS** | 0 |

**Total: 0 violations. The `post-merge-10` finding is closed.**

---

## 1. Both halves of the repair — verified independently

I rebuilt the odd-r adjacency and terrain of §2.13.2's ASCII map from the glyph
rows and ran my own Dijkstra, rather than reading any figure off the prose.

### Pair 1 — the *Ferrum Crossing* bullet

- **`(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)` is adjacency-valid.** Every step is a legal
  odd-r neighbour: (9,3)→(9,4) [row 3 odd], (9,4)→(8,5) [row 4 even],
  (8,5)→(8,6), (8,6)→(7,7), (7,7)→(6,7), (6,7)→(5,7).
- **It costs 6 MP, and 6 is minimal.** Terrain read off the map rows:
  (9,4)`F`1 · (8,5)`p`1 · (8,6)`p`1 · (7,7)`p`1 · (6,7)`p`1 · (5,7)`F`1 = 6. The
  axial distance (9,3)→(5,7) is (|−6| + |4| + |−2|)/2 = **6**, so a 6-hex,
  all-cost-1 route is exactly the geodesic. No cheaper route exists under any
  reading.
- **"reaches column 5 only at the objective itself, on row 7" — true.** The
  route's columns run 9, 8, 8, 7, 6, 5; column 5 occurs once, at (5,7).
- **"below the river's southern end at (5,5) — the river spans rows 0–5 only"
  — true, checked against the map and not the prose.** §2.13.2's key coordinates
  give Water (5,0)(5,2)(5,3)(5,5) and Bridges (5,1)(5,4); map row `r6` puts `p`
  at (5,6) and row `r7` puts `F` at (5,7). The southernmost river hex is (5,5),
  and (5,7) lies two rows below it.
- **"Excluding an edge can only RAISE a shortest path … so 6 stands under either
  reading" — sound, and the witness qualifies.** The route touches neither Bridge
  hex, so it survives edge removal at unchanged cost, and it was already minimal.
- **"the OTHER opposing route … is already Bridge-free" — true as a set
  minimum.** Under Q28 the opposing figure minimises over both East Infantry:
  (9,3)→(5,7) = 6 and (9,1)→(5,7) = 7 via
  `(9,2)(8,3)(8,4)(7,5)(7,6)T(6,7)(5,7)` (geodesic, axial distance 7). Neither
  uses a Bridge. Minimum = 6, from (9,3).
- **"West's cheapest route to North (6,2) — 6 MP from (1,3) — runs over the north
  Bridge (5,1)" — true as a set minimum.** (1,3) = 6, (1,5) = 7; the minimum is
  6 and its witness uses (5,1)`B`.

### Pair 2 — the arithmetic and the restated argument

- **14 − 5 = 9, and 9 is single-digit.** Confirmed.
- **The 14 MP Bridge-free route is real and minimal.** Re-derived:
  (2,3)1 (3,4)1 (3,5)1 (4,5)1 (5,6)1 (6,6)`m`3 (6,5)1 (6,4)`w`2 (6,3)`w`2
  (6,2)`F`1 = **14**, every step adjacency-valid. Column 5 is Water or Bridge at
  rows 0–5, so any Bridge-free crossing must pass through (5,6), (5,7) or (5,8);
  the only non-Bridge approaches to (6,2) are the Woods hexes (6,1), (7,2) and
  (6,3), all cost 2. Best decompositions from (1,3): 5 + 9 = 14 via (5,6),
  6 + 9 = 15 via (5,7), 6 + 10 = 16 via (5,8). **14 is the minimum.**
- **"5 against 14" holds as a T-SCN-11 print, not merely as a per-hex figure.**
  See §6 — this needed the one claim the author explicitly declined to make, and
  it was measured rather than assumed.
- **"South still passes at 5 against 6, exactly as drawn" — true.** Both East
  Infantry routes to (5,7) are Bridge-free, so the counterfactual moves neither.
- **The restated argument is internally consistent.** "no invariant in this stub
  reads a MARGIN — only the strict inequality" is correct: T-SCN-11's formula
  line asserts `min … > the owning lane's cost`, and asymmetry (i) states **NO
  CEILING** for it. T-SCN-06's ceiling binds the *guided* lane, not the opposing
  route. Both seats do satisfy the strict inequality either way, so the claim
  that no gate catches the counterfactual is exact.

## 2. Every new sentence written this run

All four NEW blocks were read as written text, not as diffs — the last three
findings each sat inside a sentence that had just been corrected. Beyond the
claims above, the following were checked and hold:

- "More than double" — 14 > 12. True.
- "around the river's southern end, then up through the Woods ring" — the route
  crosses at (5,6), then climbs (6,4)`w` / (6,3)`w`; (6,3) is one of the three
  named ring hexes.
- "The allowance binds ONE of this map's two objectives, the northern one."
  True — only the North opposing figure moves under a Bridge-free reading.
- **Pair 3 (Q17):** "which states as much explicitly: bridge control there is
  *tempo, not a topological wall*". §2.13.2 reads "the southern pass exists
  precisely so bridge control here is *tempo*, not a topological wall." Grounded,
  and the surrounding Q17 clauses hold too — "opposite banks are distance 2,
  inside Artillery range" (axial d((4,2),(6,2)) = 2), *The Causeway*'s Mountain
  perches at range 2–3 covering the bridge hex and reaching the far landing at
  range 3 (d((2,2),(4,2)) = 2, d((2,2),(5,2)) = 3), and *Longwater March* Water 0.
- **Pair 4 (`EQUALITY FAILS`):** the tense is now correct and the claim is exact.
  In the pre-fix set exactly one lane distinguishes `>` from `>=` — West's South
  lane (5) against East's (9,5) Infantry (5). Re-derived:
  (9,6)(8,7)(7,7)(6,7)(5,7), five cost-1 hexes, axial distance 5, so no cheaper
  route exists. All five other lanes (Ferrum North 5/6, Causeway 3/5 ×2,
  Longwater 4/8 ×2) pass under either operator. Fixture (b) is preserved and
  agrees with §4.11's "tied 5 against 5".
- No residual instance of the retracted framing survives: `double-digit` and
  `states as explicitly` each return zero matches in the master.

## 3. The integer pairs and the print convention — consistent and unambiguous

T-SCN-11's convention, stated at its definition, has one governing rule —
**"THE RELATION IS NAMED AT THE SITE, and integer order identifies nothing"** —
plus one formatting rule for the bare form: owning-against-opposing is written
bare and owning first, while measured-against-budget always writes its
right-hand term as "the 6 MP ceiling", never as a bare integer.

The two bare pairs written this run — **"5 against 14"** and **"5 against 6"** —
are both bare and both owning-first (owning = 5 in each), so each parses
unambiguously as owning-against-opposing. No new budget comparison was printed,
so the bare/labelled discriminator stays intact.

One site was examined closely and cleared: *"North's opposing figure goes from
6 to 14 against an unchanged owning 5"* puts the opposing term first. That is
**not** a breach, because it is not a bare pair — both roles are named inline
("opposing figure", "owning 5"), which is precisely what the convention's
governing rule demands, and the convention explicitly disclaims order as
information-carrying. Recorded so the Director can see it was weighed rather
than missed.

## 4. Fixture (a)'s "1 MP margin each way" — the non-edit is correct

The author's reasoning holds, and the corrected paragraph beside it does not
read as a contradiction. Fixture (a) describes only the asserted
(Bridge-permitting) reading, under which both margins are 6 − 5 = 1 — literally
true. The counterfactual now lives entirely inside asymmetry (ii)'s `WHY`
paragraph, which is labelled as a counterfactual throughout ("a Bridge-free
reading", "What the counterfactual changes") and never re-quotes fixture (a)'s
phrase. The two sites say different things about different readings, which is
the correct outcome; editing fixture (a) would have been the error.

Related tension, examined and cleared: asymmetry (ii)'s header still reads "on
the shipped map that allowance is **LOAD-BEARING** rather than merely permitted"
while the new text says no gate catches its absence. Not a contradiction — the
paragraph defines the sense it intends in its own next lines ("STATED AS A
REASON AND NOT A PERMISSION"; "the allowance is what keeps the NORTHERN opposing
route honest"), and the bullet immediately below scopes it to one of two routes.
No reader can come away believing a gate depends on it.

## 5. The register, and §4.4 / §4.11

- **Q1–Q29, each ID defined exactly once**, no gaps and no duplicates.
  **Ten ruled:** Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28.
- **Every `Q<n>` cited in the body resolves to a register row** — checked
  exhaustively across all occurrences in the master. Same for every `T-` ID:
  T-HEX-01..07, T-MOVE-01..06 (07 reserved on Q2), T-FAME-01..09, T-TURN-01..09,
  T-AI-01..06, T-SCN-01..09 + 11 (10 reserved on Q26), T-UI-01..04,
  T-DATA-01..06, T-INT-01..05, T-SAVE-01..07, T-CAP-01..08, and the T-COMBAT /
  T-REPAIR sets at `5ffa8d6`. No dead ID, and no ID cited without a definition.
- **No pinned extent.** The only Q-range in the document sits in §4.7's register
  preamble, which is the block the "single place their extent is stated" sentence
  designates. Zero ranges elsewhere.
- **Q4, Q5, Q6, Q8, Q9 state no reading and block their gates outright**, exactly
  as the preamble lists them. **Q29 blocks nothing** ("no gate — every test runs
  either way"). Q1–Q3 and Q10–Q19 carry stated conservative assumptions in force.
- **§4.4 and §4.11 still describe one schedule.** Week 1 = rows 1–3; week 2 =
  `{Move, Attack}` plus the §4.10 format and headless replayer, with T-INT-01/04
  and T-SAVE-04 closing; week 3 = rows 4–5 then row 6, closing T-INT-02/03/05,
  T-SAVE-01/03/05/06 and T-SAVE-02; week 4 = T-SAVE-07; week 5 = slot I/O only.
  Rows 9 and 10's run/close splits match §4.4's cells term for term, and the
  critical path `1 → 3 → 4 → 5 → 6/8` agrees with every row's `Depends on` cell.
- **§4.7 Stub 7 accounting is exact:** ten written invariants — six structural
  (T-SCN-01..03, 05, 07, 09) and four priced (T-SCN-04, 06, 08, 11) — matching
  §4.11's "four of its ten written invariants".
- **§3's ledger is unchanged and internally consistent:** four rows verified at
  `5ffa8d6` (Combat 10/10, Test suite 17/17, Repair 7/7, Type-effectiveness 2/2
  — and 10 + 7 = 17), eight rows `*pending*`, mapping one-to-one onto §4.7's
  eight stubs. No row claims a system built or shipped without a commit and
  passing test IDs, and Q29's conservative reading forbids a partial-pass flip.

## 6. The unfiled candidate — non-filing upheld, on a corrected ground

`tech-director` declined to file the Bridge-free cost of West's *second* Infantry
from (1,5), reasoning that "no invariant computes the counterfactual and Pair 1
keeps 'from that hex' scoping rather than claiming a set minimum."

**The outcome is right; the reasoning is one step short.** Pair 1's bullet does
keep the "from that hex" scoping, and that half of the defence stands. But
Pair 2 prints **"North still passes, at 5 against 14"** — and a T-SCN-11 print is
by construction a minimum over the opposing seat's whole CanCapture set (Q28,
ruled). That sentence therefore *does* assert a set minimum, and it needs (1,5)
to be no cheaper than 14.

I measured it. From (1,5) the cheapest Bridge-free cost to each legal crossing
hex is (5,6) = 5, (5,7) = 5, (5,8) ≥ 5, and the cheapest continuation to (6,2) is
9 from either (5,6) or (5,7) — so **(1,5) → (6,2) Bridge-free costs exactly
14 MP**, the same as (1,3). The printed minimum is correct, so no gap is being
waved past and there is nothing to file. Had the two figures differed, this would
have been a fourth finding inside a just-corrected sentence — which is exactly
why the run was slowed to measure it rather than to accept the scoping argument.

Recommendation, not a violation: if the Director ever wants the counterfactual
fully priced in the document, that is a change request to §2.13.2's table (a
Bridge-free column), as the draft says — and `scenario-designer`'s to price.

## 7. Also examined and cleared (recorded, not filed)

- **`kb_rules.md` and `kb_setting.md` are in sync.** No §2 text moved this run,
  and both files were re-checked against §2.3, §2.4, §2.7, §2.8 and §2.11.4's
  faction voicing. Every unit stat, terrain cost, defense percentage, income
  figure, tiebreak key and victory tier matches, and every `[unpinned]` marker
  corresponds to a live register row (Q4, Q5, Q6). No `kb-desync`, and no
  `voice-drift` — the four pairs are technical spec prose in §4.7 and touch no
  UI string.
- **"all Plains" / "5 hexes of Plains"** for the West South lane (§2.13.1's lane
  table, §2.11.6-B) describes a route whose objective hex (5,7) is a Factory.
  Not filed: it is a document-wide shorthand for cost-1 terrain, used only where
  every hex is cost 1; the Factory is MoveCost 1 (§2.3), the objective is named
  as a Factory at the same site, and T-SCN-06 states the accounting explicitly.
  No number is wrong and nothing downstream can misprice.
- **`sections/tech_post-merge-11_tmp.md`**, named in the draft's Handoffs as an
  artifact to delete, is absent from `sections/` — the housekeeping request was
  fulfilled. Not a `dead-reference`: it is a completed instruction inside a
  sealed addendum whose header disclaims its own currency.
- **The snapshot md5 in the sealed addendum's Grounding** (`8357f971…`) is the
  pre-merge hash and is explicitly disclaimed by the `APPLIED ADDENDUM` header.
  Not filed.
- **Re-derived and confirmed unchanged:** *Ferrum Crossing*'s terrain
  distribution (75/8/2/4/2/4/4 = 99, counted glyph by glyph), *Longwater March*'s
  (86/4/4/0/0/4/6 = 104) and *The Causeway*'s (52/4/2/6/2/2/4 = 72); every
  ρ-pair list; the axial rotation constant `W − H/2` and the mirror map
  `μ(q,r) = (q + r − (H−1)/2, H−1−r)`, both re-derived from the odd-r conversion
  and both integer-valued exactly on the stated row parity, plus the 9 × 9
  refusal at column 6.5; all eight *Ferrum Crossing* route costs and the two
  structural facts drawn from them ("+1 MP over hex distance to North", "plain
  geodesic to South"); Q21's four slack/margin pairs (1/1, 2/4, 3/2); every §4.6
  figure including $0.69, $1.725, $1.035, $178.02, $200.10 and $265.995 with the
  $1.005 and $1.24 reconciliations; §2.11.3's forecast arithmetic
  `round(10 × 1.0 × 0.8) − 5 = 3`; the 550-Fame producible force; N = 8 and
  N = 10; §2.11.6's four beats, three branches and twelve-row ledger; and §4.8's
  schema values against §2.3 / §2.4 / §2.7.

---

## Verdict

**PASS.** Every area passes, the total violation count is zero, and the single
`post-merge-10` violation is closed by a repair that is correct in both halves
and correct in every sentence it newly wrote. The most serious thing this run
turned up is not a violation but a near miss worth naming for the record:
Pair 2's `"5 against 14"` is a T-SCN-11 print and therefore silently asserts a
minimum over West's whole Infantry set, which the author's own non-filing
rationale explicitly declined to claim — the sentence is true only because West's
second Infantry at (1,5) also prices at exactly 14 MP Bridge-free, a figure that
appears nowhere in the document and that I measured independently against the
§2.13.2 map. It holds, so nothing blocks; but the next editor who moves West's
deployment or the river's southern end will move that unstated 14 with no gate,
no fixture and no sentence in the document noticing. **Nothing is required before
merge**: `source/gdd.md` at md5 `68991030a238c1804a3234db2fa0485f` is accepted as
it stands, and the master now carries no filed violation. Two items remain open
and are the Director's rather than this gate's — the title/lineage framing is
unowned and needs a `narrative-designer` this kit does not have, and the eight
`*pending*` §3 ledger rows still stand against a stock Unreal `Source/`, with
Stub 7's priced half depending on Stub 3 as the longest live dependency.
