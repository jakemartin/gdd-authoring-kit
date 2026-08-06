# Gate report — run `ue-harness-9`

`source/MANIFEST.txt` present. `gdd.md md5=7f161314451f43829497070870b5255a`.

Sections gated this run: **one**.
`sections/tech_ue-harness-ubt-and-check-repair.md` — every other file in
`sections/` was excluded by the stage prompt. No placement collision is possible
with a single section, and every pair in it names a distinct GDD site.

**Top-level verdict: PASS.** Total violations: **0**.

---

## `sections/tech_ue-harness-ubt-and-check-repair.md` — PASS

No violations.

The run-8 finding is discharged. The clause

> Facts §10 restates the *harness alone* form, and that is noted here so the two
> are not read as independent sources: §8a is the later measurement, and it is
> what these pairs follow.

no longer occurs. Whitespace-collapsed probes over the whole draft for
`restates the`, `independent sources`, `harness alone` and `Facts §10` each
return zero. The bullet now terminates at

> The seven OLD blocks those pairs replace are quoted from `source/gdd.md`, each
> matched there exactly once, as is Pair 15's, at line 2820.

which is a complete sentence; the bullet before it (`facts §8a`'s closing
paragraphs) and the bullet after it (the parity stub's `Inputs` line) are
unchanged and neither depended on the deleted clause. Nothing dangles.

### What was checked, and what it returned

**1. The deletion site and its neighbours.** Read in place. *those pairs* in the
surviving sentence still resolves to Pairs 19–25 — seven pairs, seven OLD
blocks. *Pair 15's, at line 2820* verified against the master: line 2820 of
`source/gdd.md` is *The harness is recorded here as the remaining blocker and is
not scheduled here.*, one hit document-wide.

**2. Remaining stale descriptions of the fact block.** Every `facts §` reference
in the draft is a Grounding bullet; there are fourteen and each was read against
the cited section of `uehar_facts.md`. The two the author left standing are both
accurate as written:

- *facts §8a's closing paragraphs, which supersede anything earlier in that file
  attributing the imported tables to `T-INT-02`* — the fact block says *"this
  supersedes anything earlier in this file that attributed the imported tables to
  `T-INT-02`"*. This is a governance statement over whatever earlier text exists
  and is true whether or not any such text does.
- *No ledger row moves, no register row moves, `selfplay.cpp` untouched, and the
  three modules staying unvendored: facts §10* — §10 carries all four of those
  bullets. The draft does **not** cite §10 for what `T-SAVE-06` waits on, which
  is the only bullet of §10 the correction touched.

No other bullet misdescribes the fact set. The eight-item §8a summary at draft
lines 1056–1067 was matched claim by claim against `uehar_facts.md` §8a: six
places, in-engine replay, `Replay` deliberately unvendored, non-exhaustive
statement, sweep by meaning with the definite-article tell, permissive-for-row-8
vs strict-for-vendoring, defect predates the round, judgement filed not made —
all present.

**3. Universals at any width.** The family is closed at token level and the token
level agrees with the pair set. In `source/gdd.md`, `the whole of what` occurs
six times — line 1514 (×2), 1531, 1585 (×2), 3002 — and `the editor pass alone`
twice, at 1585 and 3039. Those eight sites are exactly Pairs 19, 21, 22, 23, 24,
25 and 20, with `now the whole of what row 8 lacks` matching twice as the draft's
own Check results state and Pairs 22 and 23 disambiguating by trailing and
leading text respectively. No unrepaired member remains. No NEW block carries a
bare `alone`: every match of that substring inside a NEW block is `standalone`,
in Pairs 5, 14 and 16. Pair 15's *the remaining editor-pass IDs* quantifies over
IDs under a non-exhaustive umbrella (*among what … need besides it are*), not
over a blocker set.

**4. Counts.** §4.5's addends read off line 1585: 18, 9, 9, 6, 7, 1, 2, 1, 1, 1,
1, 4, 1 = 61, and the stated 71 / 61 / 10 figures are as the draft reports them.
Before 61, after 61, the two vacated entries replaced by one entry of 2 at
`e19605e`. The verbatim `T-INT-01` PASS line, the eight known-bad inputs (seven
FAILs plus the working-tree design control), the `--week1` per-row tallies and
the invalid-then-redone no-source control all match `uehar_facts.md` §4 exactly,
and Pair 5 closes with *no claim of coverage beyond them is made here*.

**5. Section pointers.** `pure C++17` occurs at lines 1629 and 2778 only; §4.7
begins at 1625 and §4.9 at 2729, so the draft's §4.7 / §4.9 attribution holds and
*nowhere else* is true. §4.1 (line 1544) names no language standard. `T-SAVE-06`
occurs at line 2972, inside §4.10 (2864–2980), and nowhere in §4.7 (1625–2651) —
both of the draft's claims about that pointer hold. The parity stub's `Inputs`
line (2824–2825), its invariant set `T-INT-01`–`T-INT-05` (2827–2859) and its
`Acceptance` split (2861) are as Pair 15 and change request 4 describe them.
Pair 22's `(§4.9)` pointer lands where Pair 15's `a13626f` measurement lands.

**6. Anchors.** Twelve OLD blocks were re-probed independently of the author's
report — Pairs 1, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 18 — and each matched
`source/gdd.md` exactly once. No anchor was disturbed by the run-8 or run-9
remediations, both of which are confined to prose outside the pair blocks.

**7. Format.** This file is an addendum in the established OLD/NEW form rather
than a fresh section draft. Placement is carried per pair in each `### Pair N —
§x` heading; change requests are under `## Filed change requests`; the open
judgements are filed there as change requests 3 and 4 rather than under a heading
of that name; `## Grounding` is present. Every required element is present and
locatable, so no `format-breach` is filed.

---

## Verdict

`sections/tech_ue-harness-ubt-and-check-repair.md` passes with zero violations,
and the top-level verdict for run `ue-harness-9` is **PASS**. The single run-8
violation was a stale description of the round's own fact block, and the deletion
that removed it removed the whole claim rather than rewording it, left the
enclosing bullet a complete sentence, moved no pair, no anchor, no count and no
pointer, and introduced no new claim requiring grounding. Nothing must happen
before merge beyond the Director's normal merge checklist: apply the 25 OLD/NEW
pairs at their stated placements — Pairs 12 and 14 are insertions, the rest
replacements — rebuild the `.pdf` and `.txt`, re-sync `kb/rules.md` (unaffected in
substance here, since no pair touches §2), update the §3 provenance ledger for
the two re-dated `T-INT` closures, and re-run `python sync.py`. Change requests
1–4, in particular the *editor pass* reading in change request 3, remain the
Director's to rule and are correctly filed rather than answered in prose.
