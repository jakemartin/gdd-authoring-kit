# Gate report — run `week1-build-9`

**Source of truth:** `source/gdd.md`, md5 `d3f6913b1ecf228c19811328db33b27d`,
per `source/MANIFEST.txt` (present; no `sync-missing`).

**Sections gated this stage:** one — `sections/tech_week1-build.md`. Every other
file in `sections/` carries an applied-addendum banner and is history, not this
stage's output; none was gated.

**Top-level verdict: PASS.**

---

## `sections/tech_week1-build.md` — PASS, 0 violations

### Mechanical half — re-verified in full

All thirteen **OLD** anchors were located in `source/gdd.md` and each returns
**exactly one** match:

| Pair | GDD line(s) | Anchor status |
|---|---|---|
| 1 | 1459 | unique, byte-identical |
| 2 | 1460 | unique, byte-identical |
| 3 | 1464 | unique, byte-identical |
| 4 | 1457–1458 (adjacent) | unique, byte-identical |
| 5 | 1465–1466 (adjacent) | unique, byte-identical |
| 6 | 2446 | unique as a full line (`Combat.cpp::effectiveness` also occurs at 1466; the anchor line does not) |
| 7 | 2476–2477 | unique, byte-identical |
| 8 | 1453, second half, inside the closing italic marker | unique, byte-identical; the trailing `*` is not consumed |
| 9 | 1470 | unique, byte-identical |
| 10 | 1524 | unique, byte-identical |
| 11 | 1564 | unique, byte-identical |
| 12 | 2618–2620 | unique, byte-identical |
| 13 | 1443 | unique (1 occurrence document-wide) |

- **Curly quotes:** a document-wide search of `source/gdd.md` for `’ ‘ “ ”`
  returns **zero** matches. Every anchor is straight ASCII. The draft's own
  grounding row on this point is correct.
- **Internal anchors:** `](#` returns **zero** matches document-wide, so pair 11's
  heading rewrite breaks no link target. Confirmed independently.
- **Nested fences (Director ruling 1):** pair 13 alone uses four-backtick
  delimiters (draft lines 449/451 and 453/468) and its inner three-backtick block
  (456/463) is fully enclosed. No other pair's NEW block contains a fence. Every
  NEW block has exactly one unambiguous boundary.
- **Placement collisions:** none. Pairs 1–5 take five separate lines of the
  ledger table in the source's actual row order (Combat resolution, Test suite,
  Hex, Movement, Capture & Fame, Turn loop, Opponent AI, Data tables, Repair,
  Type-effectiveness, Content/scenario, UI — verified at lines 1457–1468), so
  pair 4 sits above pairs 1–2 and pair 3 sits immediately above pair 5 without
  either OLD block spanning another pair's anchor. Pair 13 inserts at 1443,
  above pair 8's 1453 and pair 9's 1470. Pairs 6, 7, 10, 11, 12 are in four other
  sections. Every placement names a line, not a region.
- **kb-desync:** none. No pair touches §1, §2, the Q register, §4.4, or §4.11's
  build-order rows and † legend, so nothing here can make `kb_rules.md` — the
  parse of §2 — wrong.
- **Required headings:** Placement, Change requests, Open questions and Grounding
  are all present; the thirteen numbered pairs are the draft, as in every prior
  addendum this gate has accepted for this file. No `format-breach`.

### Substantive half — merging text, checked hardest

Every claim inside a NEW block was checked against `source/gdd.md` or the
Director-supplied fact set, and every one resolves:

- **Path form (Director ruling 2).** Every path in every NEW block is written in
  full. Pair 9's run-`-8` defect is repaired at the right site: the block now
  reads "resolve to two tracked files, `cpp_reference/Combat.good.cpp` and
  `cpp_reference/test_combat.cpp`, which the cells now name in full" — no
  `cpp_reference/` stated once and distributed across five bare names. Pair 4's
  Test suite cell writes all three week-1 harnesses out in full. Pair 3 writes
  all three CSVs in full. The header's "Two constructions in this file rely on
  that exemption — pair 9's OLD anchor, and the Target 4 sentence that quotes it"
  is now **accurate**: those are the only two prefix-distribution constructions
  left, and both are exempt.
- **Pair 7 (Director ruling 3).** NEW text carries no citation. `python run.py`
  survives byte-identical from the OLD anchor and is ruled in bounds; **not
  filed.** Pair 4's "All re-runnable via `python run.py`" is the same case —
  byte-derived from its own OLD anchor (line 1458), a command, repo-root — and is
  likewise not filed. Pair 7's "each §4.7 stub joins **them**" points back at
  "sources", not at a directory, so ruling 2's pronoun clause is not engaged.
- **Absolutes (Director ruling 4).** A document-wide search of the draft for
  `no path fragment`, `names nothing`, `nothing at all`, `of any kind`,
  `no file and no directory` and `contains no` returns **zero** matches. All
  seven surviving statements about pair 7 and pair 13 use the sanctioned narrow
  form "cites no path" (draft lines 262, 267, 275, 439, 560, 587, 658). The three
  over-claims filed at run `-8` are gone, not merely softened. "The element is
  gone rather than narrowed" (line 273) is bound by its definite article to the
  single path-shaped element named in the preceding clause and does not assert
  the NEW text is free of path fragments; **in bounds, not filed.**
- **The bare-citation tally.** Counted independently from `source/gdd.md`: line
  1457 carries two (`Combat.cpp`, `test_combat.cpp`), 1458 one, 1465
  `Combat.cpp::repairAmount`, 1466 `Combat.cpp::effectiveness`. **Five citations,
  four cells, two tracked files.** Pair 9's NEW states exactly that. The three
  units are kept distinct everywhere they appear.
- **Probe coverage.** After the pairs apply, every path the ledger table cites is
  probed at the commit its own row names: pairs 1–3 and pair 4's week-1 half at
  `c224825` (fact E), pairs 4–6's Combat half at `5ffa8d6` (fact D). The five
  rows still reading `*pending build*` cite no path. Pair 9's "every path this
  table cites was probed at the commit its own row names" is therefore true as
  written.
- **Absence claims.** "Neither bare name has ever existed in this repository at
  any commit" rests on fact C's whole-history enumeration, which is the extent
  that claim needs; "The `build/` directory is not tracked at all" rests on fact
  F (0 at both commits, 0 ever added). Both carry their stated extent.
- **`Test Engineer` in pair 9.** Checked as a candidate `contradiction`, since
  the same sentence says the week-1 modules were **not** a live CrewAI run.
  It is **not** one: `source/gdd.md` line 1383 gives the Test Engineer's
  instrument as "**Claude Code + test harness**", and line 1407's test-first
  workflow is "Director writes a spec → Test Engineer writes tests against it →
  Systems Engineer implements until tests pass" — precisely the shape fact A
  describes. The `python run.py` pipeline attribution is grounded in line 1458
  and line 2477 ("the `g++`/`clang++` + `python run.py` gate runs (§3 ledger)"),
  which the OLD pair-7 anchor extends to "each §4.7 stub as it lands". **Not
  filed.**
- **Arithmetic.** Re-derived from §4.11's Acceptance cells, not from the draft:
  T-HEX 7, T-DATA 6, T-MOVE 6, T-FAME 9, T-TURN 9, T-AI 6, T-SCN 10 (01..09 + 11),
  T-UI 4, T-INT 5, T-SAVE 7 = **69**. Rows 4–10 = **50**. Rows 1–3 = **19**, of
  which **18** are green at `c224825`, leaving **69 − 18 = 51**. Pairs 8, 10 and
  12 and the informational table all state these consistently. Six `✓` rows and a
  seventh carrying evidence without one is correct after pairs 1–3.
- **Cross-references.** Verified live, not assumed: Q29's "full acceptance set at
  one commit" (line 2649, the T-DATA-05 † bullet, which is *below* the preamble
  pair 12 replaces — so pair 12's "its † bullet below" resolves); T-DATA-05 as the
  in-editor Unreal Automation parity pass (lines 2399, 2461, 2467); T-MOVE-07
  reserved on Q2 (lines 1663–1666, 2363); row 4 depends on row 3 alone (line
  2634); row 7 depends on rows 1, 2, 3 (line 2637); row 10(a) "no deps at all;
  write it first" (line 2640); "the scenario row flips after movement, not
  before" (line 2704); §2.3 is the terrain/move-cost section (line 141), so pair
  13's "not the §2.3 rule" resolves. No dead reference.
- **Compiler set.** "Under clang++ and MSVC both" is fact B verbatim; the residual
  tension with the three `g++`/`clang++` sites is **filed as a change request**,
  not written into their prose. That is the correct handling and is not a
  violation.
- **Voice.** Declarative, present-tense, matching the register of §3 and §4.11.
  Pair 13's inserted block mirrors the existing T-COMBAT-07 example's format. No
  `voice-drift`.

---

## Verdict

`sections/tech_week1-build.md` **PASSES** with **zero violations**, and the
run-level verdict is **PASS**. Nothing must happen before merge: the thirteen
pairs may be applied at the placements given, with the bar-(b) sign-off decision
and its five coupled fallback sites resolved by the Director at merge time as the
draft's own fallback table sets out. On the standing question — the apparatus is
now generating more risk than it retires. Across nine runs the thirteen
replacement pairs have drawn exactly two findings, both real and both repaired
(run `-6`'s group label, run `-8`'s `cpp_reference/` prefix-distribution in pair
9); every other finding has been in self-descriptive commentary that never
merges — headers counting their own exemptions, summaries restating pair 7's
scope in three places, grounding rows narrating their own extent. Those sites
have no reader downstream of the merge, and each is a fresh surface for an
absolute to creep back onto. Stripping the file to the thirteen pairs, the
placement table, the change requests, the open questions and a grounding note
that cites the fact sections by letter would retire that surface without
weakening a single thing that merges.
