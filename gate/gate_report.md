# Gate report — run `t-int-01-widening-4`

- Master: `source/gdd.md`, MANIFEST md5 `0121ee5b372b3a1ed8d15975587c3f88`.
- `source/MANIFEST.txt` present; all three source files listed. No `sync-missing`.
- Sections read: `sections/tech_t-int-01-widening.md` (17 pairs).
- Top-level verdict: **PASS**. Zero violations.

---

## `sections/tech_t-int-01-widening.md` — PASS (0 violations)

No violations filed.

### What was checked and what it resolved to

**The run `-3` violation is closed.** Run `-3` filed one `stat-drift`: §3's
`b23823f` landing record read

> its green count moves 53 → 55 and its unclosed count moves 18 → 16

while Pair 13 credited one closure to that commit and one to `d837fc8`. Pair 17
takes that exact string as its OLD and replaces it with

> its green count moves 53 → 54 and its unclosed count moves 18 → 17

and Pair 4 now carries the other half explicitly:

> its green count moves **54 → 55** and its unclosed count moves **17 → 16**,
> which is the second half of the movement whose first half the `b23823f`
> landing above records

The two records agree with each other and with Pair 13's split (`**1**` at
`b23823f`, `**1**` at `d837fc8`). The clause run `-3` was silent about — Pair 4's
former "no count moves either way" — is gone rather than annotated, and no
figure is stated twice inside Pair 4.

**Per-landing green chain, read off the merged text**, is contiguous end to end:
18→27, 27→36, 36→42, 42→49, 49→50, 50→52, 52→53, 53→54 (Pair 17), 54→55
(Pair 4). No gap and no overlap introduced.

**§4.5's green breakdown re-derived from the merged §4.5 cell**, not from the
draft's arithmetic: 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 + 1 + 1 = **55**, matching the
cell's own `**55** of the 71 are green`. Totals 71 written / 55 green / 16
unclosed are unmoved, and 71 − 55 = 16 holds, so no §4.5 total is owed a pair —
the draft's Arithmetic table states exactly this.

**Per-landing unclosed chain** reads 21→20, 20→18, 19→18, 18→17, 17→16 after
merge. The 20/19 step is byte-identical in the master before these pairs are
applied and is explained in place by §4.5's own risk cell — `T-UI-05` "widened
this gap by one when it was written and closed it again there, and those two
movements are counted separately rather than netted". Pre-existing, not this
draft's, and not a finding.

**Placement collisions.** Pairs 2, 4 and 17 all edit the single §3 paragraph at
`source/gdd.md` line 1514. Their OLD strings are disjoint substrings in document
order — Pair 2's `Whether the ledger should gain the row is filed for the
Director.`, then Pair 17's count sentence, then Pair 4's `How `e06c44b` and
`b23823f` were authored…` at the paragraph's end. Pair 4's forward reference to
"the `b23823f` landing above" resolves, because Pair 17's site precedes it in the
same paragraph. Pairs 13 and 14 edit two disjoint clauses of the §4.5 cell at
line 1585. No collision, and every placement is a verbatim anchor rather than a
prose direction.

**Every OLD located in `source/gdd.md`**, each once: Pair 1/2/4/17 at line 1514,
Pair 3 at 1531, Pair 12 at 1566, Pairs 13–14 at 1585, Pairs 5–6 at 2737–2742,
Pair 7 at 2787, Pair 8 at 2554, Pair 9 at 2600, Pair 10 at 2645, Pair 11 at 2609,
Pair 15 at 2933, Pair 16 at 2961.

**Deletion sweep re-run mechanically, not taken on the draft's word.** Every
occurrence of `T-INT-01` (20), `99fcb84` (8), `thirty-two` (1) and `Q32` (4) was
enumerated and classified. Every present-tense green credit or vendored-tree
claim is covered by a pair; what is left uncovered states what a past landing
did — the three `99fcb84` mentions inside §3's `b23823f` record, and the
`2/2 under clang++` gate tally at that commit, which is a count of checks run and
not a claim of two closures, the distinction §3 already draws at
`GATE-AI-SMOKE` and at row 8's `34/34`. Line 1566's `T-INT-01/04 and T-SAVE-04
close here` is a week-2 schedule statement with no commit and is correctly left.
Lines 2813, 2837 and 2994 name the IDs without crediting a commit. No stale site
survives the pairs.

**Register extents.** `thirty-two` occurs once (line 2600, Pair 9) and no other
site states the register's row count, so Pair 9 is the whole of the extent edit.
Ruled 16 + open 17 = 33; the open list Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31, Q32
enumerates to 17. Pair 11 states Q33's disposition without restating a figure.

**Grounding, claim by claim.** `99fcb84`'s reachability (Pair 3) is grounded in
the measured `merge-base --is-ancestor` and the `99fcb84` → `6f6dd58` →
`9dec48c` chain; `9dec48c` is the head, so "each is reachable from the head" is
true of both. The manifest's unmatchability (Pairs 6, 7) is grounded in §4.10's
own `rulesCommit` row — "Crew commit of the rules module that wrote the file" —
verified at line 2837. Pair 10's "runs on every gate run" is grounded at §4.9's
`Acceptance: T-INT-01, 04 on every gate run` (line 2813). Pair 15's precedent is
grounded in §4.11's own `T-TURN-01..09` sentence (line 2922). Pairs 4 and 17's
per-landing convention is grounded in §3's own rows 4–9 landing sentences. The
22-file coverage decomposes against §4.9's ten modules × 2 plus `StratRules.Build.cs`
plus the manifest. No substantive claim is ungrounded.

**Change requests, not prose changes.** Four items are filed for the Director —
the §4.9 by-construction clause, the deferred row's name and acceptance set, the
bridge's gateability, and whether the re-dating should become a general
convention. Each is a proposal to move or add something the GDD does not state,
and none of them is enacted in the pairs. That is the correct channel and files
no `stat-drift`.

**`kb_rules.md` / `kb_setting.md`.** This addendum touches §3, §4.4, §4.5, §4.7,
§4.9 and §4.11 only. `T-INT-01`, `b23823f`, `acceptance ID` and `provenance
ledger` return zero matches in `source/kb_rules.md`, which is a parse of §2. No
`kb-desync`.

**Voice.** Declarative and present-tense throughout, matching §3's and §4's
register. No UI strings are written.

---

## Verdict

**PASS.** `source/MANIFEST.txt` is present, `sections/tech_t-int-01-widening.md`
carries zero violations, and the top-level verdict is therefore PASS. The single
`stat-drift` filed at run `-3` is closed by the Pair 17 split, and the split is
consistent in both directions: §3's per-landing chain now steps 53 → 54 at
`b23823f` and 54 → 55 at `d837fc8`, reaching the same §4.5 totals — 71 written,
55 green, 16 unclosed, 9 verified ledger rows — that the master already states
and that this addendum does not move. Nothing must happen before merge beyond
the Director's ordinary merge checklist: apply the 17 pairs at their stated
anchors, rebuild `.pdf` and `.txt`, re-sync `kb/rules.md` (unaffected here, but
the step stands), leave the §3 ledger table unflipped as Ruling 2 requires, and
re-run `python sync.py`. The four change requests are the Director's to rule on
and are not conditions of this merge.
