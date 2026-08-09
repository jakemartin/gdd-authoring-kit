# Gate report — run `bridge-scope-9`

- `source/MANIFEST.txt`: present. `gdd.md` md5 `417a3ad795303c1012dd84520108499a`.
- Sections read this round: `sections/tech_bridge-scope.md` (39 pairs; §3, §4.4,
  §4.5, §4.9, §4.11).
- Top-level verdict: **PASS**.

## sections/tech_bridge-scope.md — PASS, 0 violations

No violations filed.

## Record of what the ruling turned on

Findings are absent, so this section records the checks whose outcome the ruling
rests on rather than restating them as merits.

**Sweeping method.** Every sweep below was run newline-insensitively over the
hard-wrapped master. The line-oriented form of the `re-date` sweep returns 6
sites; the multiline form returns 13, and the extra 7 include §4.9 part 1's
`2830`–`2834` pair, §4.9 part 2's `2942`, and §4.11's `3193`. Three findings-
relevant sites were visible only in multiline mode.

**Pair 39 against Pair 7.** Pair 7 rewrites §3's `fed8ae9` record to
`did not re-date there: both were green at [e19605e]…`; Pair 39 rewrites §4.9
part 1's twin (master line 2870) to `did not re-date on that removal (§3).`
Both pin the same claim to the same event — the `.uproject` `Modules`-array
removal at `fed8ae9` — and neither asserts a current date, so neither collides
with Pairs 11, 12, 17, 19, 22, 29 or 31, which date the re-dating that did occur
to the `0897cb5` vendoring and credit both greens at `9289c1d`. Pair 39's `(§3)`
cross-reference resolves, after merge, to Pair 7's sentence, which agrees with
it. Pair 39's OLD is contiguous on master line 2870 (no wrap inside it), and the
`T-INT-01` and `T-INT-04` do not re-date prefix occurs twice in the master —
1516 and 2870 — but only 2870 is followed by ` (§3).`, so the full OLD is unique.
The link-dependency clause preceding it is untouched, per CR-4.

**The `re-date` family, 13 sites, verified multiline.** Seven on master line
1516 (six self-pinned §3 landing records; the seventh is Pair 7's OLD), one at
1589 (Pair 17's OLD), two at 2833–2834 (inside Pair 22's OLD), one at 2870
(Pair 39's OLD), one at 2892 (`both T-INT closures re-dated as a result`, past
and scoped to its own round), one at 3218 (Pair 31's OLD). No uncovered site
remains.

**Falsification sweep for the `0897cb5` landing.** Swept multiline for
`bridge consumer`, `command surface`, `no bridge`, `unbuilt`, `unvendored` /
`not vendored` / `vendored set`, `ten crew modules` / `eleventh` / `twelfth` /
`thirteenth` / `22 files` / `20 sources`, `replayer`, `e19605e`, `a13626f`,
`did not run` / `no editor pass` / `does not exist`, `§4.9 part 2`,
`game module` / `Stratocracy` module / `UBT module`, `StratRules`, and
`T-SAVE-06` / `T-INT-02` / `T-INT-03`. Every live (non-commit-pinned) site is
inside a pair's OLD. The remaining hits are landing records pinned by their own
commit, verbatim quoted PASS lines, or terrain `Bridge`.

**Closure versus ran-and-passed, under CR-1.** Every site the draft touches
states run-and-passed-without-closing: Pairs 11, 13, 15, 18, 20, 23, 26, 30, 32,
34. §4.5's figures in the master read **71**, **62**, **9**, with **3** in row 9
and **1** in row 10; the draft moves none of them. Q29's register text at master
line 2662 reads `a partial pass is reported as a run and never as a closure`,
which is what Pair 11 cites.

**The two events.** The draft keeps crew `f5fdb69` as the declaration
(`excluded` → `vendored`) and UE `0897cb5` as the byte movement, at all three
sites that name both (Pair 11 twice, Pair 22 once). No site attributes bytes to
`f5fdb69`. Both claims about `ue_module/vendored_set.json` — its two modifying
commits and `Balance` among the `excluded` keys at `e19605e` — appear only in
Pair 11's naming record and are carried in the grounding table's last row.

**Apparatus.** 723 → 737 lines. Pair 39's block occupies exactly 14 lines
(separator, heading, anchor, OLD fence, NEW fence and their blanks) at draft
lines 452–465. The grounding table gained no row; its `fed8ae9` row was amended
in place. The growth is inside the pair.

**KB.** `source/kb_rules.md` contains no `T-INT`, `StratRules`, `vendor` or
bridge-system text — its three `Bridge` hits are the §2.3 terrain row. This
draft touches §3 and §4 only, so no `kb-desync` arises.

## Verdict

`sections/tech_bridge-scope.md` passes with zero violations, and the run's
top-level verdict is **PASS**. Before merge, the Director applies the 39
old→new pairs to `../stratocracy-content/Stratocracy_Prototype_GDD.md` at the
anchors each pair names, verifying each OLD as a literal string against the
master rather than by eye — Pair 39's OLD in particular shares a prefix with the
§3 site at master line 1516 and is distinguished only by its trailing ` (§3).`
Pair 11's insertion goes immediately before `Legend: **Author**` at the end of
§3's ledger prose, and Pair 22 and Pair 39 both land in §4.9 part 1 and must
both be applied, since applying one without the other leaves that section
asserting a present-tense `do not re-date` beside a past-tense record of the
re-dating that did occur. Then rebuild the `.pdf` and `.txt`, re-sync
`kb/rules.md`, leave the §3 provenance ledger unchanged — CR-3 creates no row
and CR-1 flips none — and re-run `python sync.py`. The two open questions the
draft files, `GATE-BRIDGE-DEFS`'s acceptance ID and the owner of a parity
fixture carrying `Capture` and `Build`, are for the Director and do not gate
this merge.
