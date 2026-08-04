# Gate report — run `row8-record-2`

- **Master**: `source/gdd.md`, md5 `83899833551abbe9d4518e21fd771520` (from
  `source/MANIFEST.txt`), which is the md5 the draft's Placement declares.
- **Sync**: `source/MANIFEST.txt` present — three entries, `gdd.md`,
  `kb_rules.md`, `kb_setting.md`. No `sync-missing`.
- **Sections gated**: one — `sections/tech_row8-record.md`, thirteen pairs.
- **Top-level verdict**: **PASS**. 0 violations.

---

## `sections/tech_row8-record.md` — PASS (0 violations)

No violation is filed. What follows is the record of what was checked, since a
PASS is only as good as the checks behind it.

### The four `row8-record-1` violations, re-checked at the source

**1. `contradiction` — the clause Pair 3 left standing. Cleared.** Pair 3's OLD
now reads, verbatim and matching `source/gdd.md` line 1511 exactly once:

> everything on that path but **row 8** is now evidence rather than schedule —
> **per acceptance ID as well as per row**, since `T-TURN-10`, the one path ID
> that was written and asserting without being green, closed at `6ccd40b`

and its NEW restates the tail rather than leaving it:

> **per acceptance ID as well as per row**: `T-TURN-10` closed at `6ccd40b`, and
> the path IDs still written and asserting without being green are **T-UI-03**
> and **T-UI-04**

That restatement is true against the source: §4.11's chain is
`1 → 3 → 4 → 5 → 6/8` (line 2824), and of the IDs on rows 1, 3, 4, 5, 6 and 8
the only two written, asserting and not green are T-UI-03 and T-UI-04 —
T-MOVE-07 is reserved-**unwritten** on Q2 (line 2480) and so does not answer the
description, which the draft keeps distinct in Pair 7 and Pair 4.

**2. `invented-fact` — the driver's `snapshot` command. Cleared, and the round-1
finding was mine on a short fact set.** The Grounding now carries a paragraph of
its own for it, and it does not exceed the fact: the command prints §4.7 Stub 8's
view model; `scenario snapshot` is the same command under row 7's spelling, which
refused on row 8's account at `9086d6a` and does not at `7c36303`; `GATE-DRV-12`
is new at this commit and asserts the driver holds no view model of its own, by
rebuild through `cpp_reference/Ui.h` and by the one-of-two-flags case;
`GATE-DRV-01..12` is 12/12 under clang++ and MSVC both; the IDs are not `T-*`.
Pair 4's prose claims no more than that, and the master's `GATE-DRV-01..11,
11/11` at `6ccd40b` (line 1511) is the count it moves from.

**3. `invented-fact` — the `critical path` sweep. Cleared and exact.** The string
occurs at **19** occurrences over **17** lines in `source/gdd.md`, with lines
1511 and 2501 carrying two each, plus the capitalised `Critical path:` at 2824.
The draft's enumerated line list — 30, 71, 97, 485, 1505, 1511, 1551, 1564, 1570,
1579, 1582, 1644, 2359, 2501, 2623, 2752, 2838 — is the grep result exactly, and
the three it names as previously missed (1644, 2359, 2623) are the §4.7 cut-line
rule, Stub 7's MCP note and §4.9's editor-only-tooling note. None states what has
been built; each was read in the text that would falsify it.

**4. `invented-fact` — the `GATE-CAP-PARTIAL` sweep. Cleared and exact.** Eight
lines: 392, 400, 2395, 2405, 2464, 2484, 2492, 2775 — the draft's list, with the
two previously omitted (2484, Q6's Assumption cell; 2775, §4.11's build-order row
8) now named with their reasons. Q6's cell records where the gate lives and the
date that home was ruled, not whether it ran, so the landing does not falsify it;
§4.11's row lists the acceptance set, which the addendum's own Build order
section confirms unmoved.

### What the revision could have disturbed, re-checked

- **Does the extended Pair 3 leave any further clause standing whose truth
  depended on the exclusion it removes?** No. The surviving continuation is
  `, and row 8's other dependency is **row 7**, which has since landed at
  \`9086d6a\` on a partial pass` — true independently of whether row 8 has
  landed, and confirmed against §4.11's dependency cell `5, 7` (line 2775).
  Upstream in the same sentence, `at \`d8284f1\` only rows 7–8 hold none` is
  commit-scoped to `d8284f1` and unaffected. The other three sites that assert
  row 8's position on the path are Pairs 10 (line 1582), 13 (line 2752) and the
  §2.10 bullet at line 487, which states only that row 8 *depends on* row 7 and
  stays true. `rows 7–8 depend on landed code rather than on scheduled code`
  (line 2751) is outside Pair 13's block and remains true.
- **Pair 3 is still a replacement.** Its extended NEW does not contain its
  extended OLD as a substring. Pair 4's NEW opens with its OLD verbatim and is
  the only insertion. Twelve replacements, one insertion, as the Grounding's
  re-derived classification paragraph states.
- **Anchor uniqueness, spot-checked at the source** on the short and
  collision-prone anchors: `It has not run, so` (line 401), `**50** of the 70 are
  green` (1582), `**Reduced and re-scoped at 2026-08-03, not retired:**` (1582),
  `**Nine rows carry a ✓ …` (1528) and `| UI | *pending* | — | *pending build* |`
  (1526) each match one line. Pairs 8, 9 and 10 share the one §4.5 cell and their
  spans are ordered and disjoint, with the untouched `18 / 9 / 9 / 6 / 7`
  enumeration between Pairs 9 and 10, as claimed. Pairs 1, 11 and 13's multi-line
  anchors match the source line breaks exactly.
- **`*pending*` sweep**: four lines — 71 (§1.7's revision-note row), 1526 (§3's
  UI row, Pair 5), 1622 (§4.7's dated heading), 2741 (§4.11's opening). Only
  1526 moves; the other three are dated records of a past state. §4.11's
  `rows 1, 3, 4, 5 and 6 have since flipped` (2743) stays complete because row 8
  does not flip.
- **Arithmetic** (re-derived, not carried): green `18 + 9 + 9 + 6 + 7 + 1 + 2 =
  52`; unclosed `1 + 3 + 2 + 12 = 18`; `52 + 18 = 70`; rows 9–10 hold
  `T-INT-01..05 + T-SAVE-01..07 = 12`, and the old `16` in rows 8–10 decomposes
  as `12 + T-UI-01..04`. §4.5's `**70** written acceptance IDs` and `against
  **9** verified ledger rows` correctly do not move. Pair 6's `two more` →
  `three more` is right against the table's three evidence-without-✓ rows.
- **`kb-desync`**: none. `T-CAP-05`, `GATE-CAP-PARTIAL` and `T-UI-0*` occur zero
  times in `source/kb_rules.md`, verified directly on the current bytes. Pair 1
  changes only run state, not a rule. Open question 5 correctly leaves the
  §2-touched re-sync to the Director rather than asserting it away.
- **`scope-breach`**: none. Pair 1's §2.8 edit is inside the blast radius the
  landing creates and is declared as such in Placement and in the rules-designer
  handoff. No spec stub is redrafted, no acceptance ID minted, no † mark or
  dependency moved, no §4.4 ruling written; the Build order section reproduces
  §4.11's row 8 unchanged.
- **`format-breach`**: none. Placement, Draft, Change requests, Open questions
  and Grounding all present; sites named to the cell.
- **`placement-collision`**: none. One section in this run; the thirteen spans are
  distinct and each is anchored to text, not to a section number.
- **`unverified-claim`**: none. Every green claim carries `7c36303` and named
  IDs, and the two that did not run — T-UI-03 and T-UI-04 — are stated as not
  run, in the same words at all four sites that mention them.
- **`voice-drift`**: none. Declarative present tense throughout, matching §3 and
  §4's register.

---

## Verdict

**PASS**, one section, zero violations. The revision does what the block
required and nothing beyond it: Pair 3's span now carries the `T-TURN-10` clause
and restates it against the two path IDs that inherit its description, the
driver's `snapshot` command is grounded to the same standard rows 4, 5 and 6 hold
for the commands they introduce, both Grounding sweeps now reproduce the grep
exactly at seventeen and eight lines with the missed sites named, and the
insertion/replacement split is re-derived from the current bytes rather than
carried forward. Nothing further must happen before merge: the Director may apply
all thirteen pairs against `source/gdd.md` md5 `83899833551abbe9d4518e21fd771520`,
post-checking that Pair 4's anchor survives once and the other twelve OLDs are
absent, then rebuild `.pdf`/`.txt`, decide open question 5 on whether Pair 1's §2
edit obliges a `kb/rules.md` re-sync, and re-run `python sync.py`. This file is
not safe to apply twice.
