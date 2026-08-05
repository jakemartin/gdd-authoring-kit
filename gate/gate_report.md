# Gate report — run `row9-integration-4`

- Master: `source/gdd.md`, md5 `8db63b1a1b3122fb656cea3961e8e45f` (per `source/MANIFEST.txt`)
- Sections gated this stage: `sections/tech_row9-integration.md` (1)
- **Top-level verdict: PASS** — 0 violations.
- Prior runs: `-1` BLOCK/7, `-2` BLOCK/4, `-3` BLOCK/1. The one surviving
  violation is resolved.

`source/MANIFEST.txt` is present, so the run is not stale. Anchor existence —
11 OLD blocks, each extracting under a strict matcher and occurring exactly
once — was verified mechanically by the Director and is not re-derived here.
Findings withdrawn in earlier runs (the `T-INT-03` ruling, the log-scoping
carve-out, and the `c224825` substitution ruled correct in `-3`) stay withdrawn
and were not revisited.

---

## sections/tech_row9-integration.md — PASS (0 violations)

### 1. The `-3` violation is resolved, and nothing was substituted for it

Run `-3` filed one `invented-fact` against Grounding bullet 4's final clause:

> `spec/integration_spec.md` records that derivation; it does not supply it.

That string does not occur anywhere under `sections/`. A search for
`integration_spec` across the kit returns hits only in `gate/gate_report.md`
and `gate/accept.json` — this gate's own prior record — and one hit inside the
draft, at Pair 2's NEW text, discussed below. Bullet 4 now terminates at:

> …which between them exclude every `test_*.cpp`, `driver_main.cpp` and
> `selfplay.cpp` and leave the ten modules' headers and good implementations.

No replacement pointer, no demoted restatement, no relocation of the claim to
another bullet, another pair note, or the check-results list. The fix ordered
was a deletion and a deletion is what was made.

The bullet still carries its grounding without the deleted clause. Its §4.9
citation is verbatim in the master, wrapping a line break at `source/gdd.md`
2735–2736:

> `StratRules` contains **no engine headers, no UObject, no third-party
> includes** — pure C++17 in `namespace strat`, exactly the base-spec constraint.

and the UBT single-`main()` constraint is stated in the standing fact block.
The deletion therefore removed the only ungrounded element and left a bullet
that is a citation, which is what the apparatus limit requires of Grounding.

### 2. No new finding was introduced by the deletion

**The surviving `spec/integration_spec.md` mention is a landing claim, and the
author's argument for it is correct.** Inside Pair 2's NEW text:

> New in the crew repo: `sync_stratrules.py`, `spec/integration_spec.md`,
> `run_integration_gate_fn` in `crew/tools.py`, and `python run.py
> --integration`, which `--week1` now also runs at its end

Against the record:

> COMMIT `b23823f` — build-order row 9's headless half. New:
> `sync_stratrules.py`, `spec/integration_spec.md`, `run_integration_gate_fn`
> in `crew/tools.py`, and `python run.py --integration`, which `--week1` now
> also runs at its end.

The draft asserts that the file is new at that commit and asserts nothing about
what is inside it. That is exactly and only what the record establishes, in the
same enumeration and the same order. It is grounded by Grounding bullet 2 —
*"Row 9's headless half, its new files and entry points: commit `b23823f`"* —
which is a citation to a commit, not to a file's contents. Nothing is owed
here; the distinction the `-3` violation turned on is the distinction the
surviving sentence respects.

**The deletion orphaned nothing.** No pair, note, check result or change
request cites `spec/integration_spec.md` as the source of the vendored-set
derivation, or of anything else. The derivation itself is stated once, in Pair
9's NEW — *"Nothing else is vendored — a UBT module cannot hold a second
`main()`, which excludes every `test_*.cpp`, `driver_main.cpp` and
`selfplay.cpp`, and the `*.buggy.cpp` files are pass-1 fixtures"* — and bullet
4 is its citation. Removing the clause left that pairing intact.

**The bullet count is what a single-clause deletion predicts.** Grounding holds
eleven bullets: runner repair; row-9 landing and the UE-repo tree; the gate run
and control results; the vendored set; the Director rulings; §4.9's
any-one-compiler clause; the run-versus-close split and the † bullet; the
log-scoping universal at both sites; `T-DATA-01..04, 06` at `c224825`; Q29's
per-ID reading; the post-repair tally cross-check. Bullet 4 plus the other ten,
none added and none merged away.

### 3. The claim of "byte-for-byte unchanged elsewhere" is verified, not taken

Checked against run `-3`'s own quotations of the draft, clause by clause, in
every place `-3` recorded text it had cleared:

- **Pair 2 seam.** OLD still ends *"rather than preserved in place from
  `7c36303`.*"*; the NEW still restores the italic close, terminating at *"…no
  harness claim is made for either, because none was established.*"*.
- **Pair 3.** Still reads *"Every **crew-repo** commit this section **cites** …
  reachable from the head of `main` there"*, *"`99fcb84` … is reachable from
  the head of `master` in the **Stratocracy** UE project repo"*, and *"the first
  citation this ledger makes outside the crew repo"* — the three clauses on
  which `-3` cleared the reachability universal.
- **Pair 9.** OLD still ends at *"records the source commit\nhash."*; the NEW
  still carries the single-sited object-store sentence *"which reads each source
  from the git object store rather than the working tree — so identity is true
  by construction at the moment the script finishes"*.
- **Pair 11.** OLD still runs through *"T-DATA-01..04 and 06 pass\nat that
  commit and T-DATA-05 has not run,"* and the NEW still names `c224825`.
- **Check results.** All fourteen bullets stand, including the log-scoping
  sweep (*"occurs twice"*, no carve-out owed) and the † bullet reconciling
  `T-INT-03`, both of which state the master's position and assert no ruling.
- **Change requests.** Three, unchanged, including the `T-INT-01` UE-owned
  exemption that `-3` confirmed still carries the deleted-from-prose claim.

Independently against the master, `source/gdd.md` line 1585 still reads *"**53**
of the 71 are green"*, *"**18 IDs remain unclosed**"*, *"the **12** in rows
9–10, which hold no code"* and *"**71** written acceptance IDs … against **9**
verified ledger rows"*, so every OLD the arithmetic depends on is the master's
current text and no pair's premise moved under it.

### 4. The arithmetic still chains

| Quantity | Before | Movement | After |
|---|---|---|---|
| Written acceptance IDs | 71 | none minted | 71 |
| Green | 53 | + `T-INT-01`, `T-INT-04` | 55 |
| Unclosed | 18 | − `T-INT-01`, `T-INT-04` | 16 |
| Verified ledger rows | 9 | no flip | 9 |

The master's breakdown sums 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 = 53; Pair 5's added
**2** at `b23823f` takes it to 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 + 2 = 55, which is
Pair 4's total. The master's unclosed enumeration sums 1 + 3 + 2 + 12 = 18;
Pair 7 splits the 12 into 3 + 7, giving 1 + 3 + 2 + 3 + 7 = 16, which is Pair
6's total and the complement 71 − 55 = 16. Row 9's five written IDs split 2
closed / 3 not, and 5 + 7 = 12 reconciles the figure Pair 7 retires. Fourth
pass, unchanged and clean.

### 5. The apparatus limit's three species are clean

- **Counts outside the arithmetic section.** None. Pair 4's note defers
  (*"Derivation in the arithmetic section"*); the sweep bullet's *"occurs
  twice"* counts occurrences of a swept string, not IDs; the `-3`-cleared
  §3 sweep bullet quotes the master's *"Nine rows carry a ✓"* and *"Eight IDs
  are still recorded as **uncovered**"* as the sweep's object, not as a tally
  of this round's work.
- **Restatements of a definition a pair states.** The object-store read is
  single-sited in Pair 9; Pair 2 states the check's non-trust of the manifest
  hashes, which is a different mechanism and is stated once. The not-wired
  definition sits in Pair 2 alone; the vendored set in Pair 9 alone, with Pair
  2 pointing to it rather than repeating it (*"the vendored module itself is
  described in §4.9"*). Grounding names these as citation labels, which the
  limit permits.
- **Inference from one passage to another.** The two comparing bullets — the
  log-scoping universal at its two sites, and §4.11's † bullet against §4.9's
  Acceptance line — report the sweeps the brief required and ground no claim
  on the comparison; both end by stating that no pair asserts anything there.

The deletion touched none of the three and introduced no fourth site of
anything.

---

## Verdict

**PASS.** `sections/tech_row9-integration.md` carries zero violations and the
addendum is clear to merge. The single deletion ordered in run `-3` was made
exactly and only as ordered: the clause claiming `spec/integration_spec.md`
*"records that derivation"* is gone from the draft with nothing put in its
place, no pointer relocated to another bullet, and no orphaned citation left
behind — Grounding bullet 4 now rests on a §4.9 quotation that is verbatim in
the master and on the UBT single-`main()` constraint, which between them carry
it. The one surviving mention of that file, inside Pair 2's NEW text, is a
landing claim that reproduces the record's own enumeration of what is new at
`b23823f` and asserts nothing about the file's contents, so it is not the
`-3` finding in another dress. Every other element the author reported
unchanged was re-checked against run `-3`'s quotations and against the master
rather than taken on report — the eleven pairs' seams, the fourteen check
results, the three change requests, the remaining ten grounding bullets — and
the arithmetic chains a fourth time at 71 / 55 / 16 / 9 with both enumerations
summing to their totals and the complement holding. Before merge the Director
need do nothing to this file; it should be merged at the eleven placements as
written, after which the three unresolved change requests — the `T-INT-01`
UE-owned exemption, whether §3 gains a row for build-order row 9, and whether
the exemption question becomes a numbered register row — remain open for the
Director's own hand, and `kb_rules.md` must be re-parsed only if §2 moves,
which this addendum does not touch.

---

## Post-verdict clarification — `T-INT-03` is not an unresolved defect

An earlier draft of the closing paragraph above added, to the list of things
left for the Director, "the filed §4.11 / §4.9 disagreement over `T-INT-03`."
The Director challenged that against this gate's own run `-1` finding. **The
challenge is correct and the remark was loose phrasing; it is struck from the
paragraph above.** The master states a coherent position and contains no known
falsehood on this point. Nothing else in the report or in
`gate/accept.json` changed, and the verdict is unaffected.

The two passages, both unchanged by this addendum:

> Acceptance: T-INT-01, 04 on every gate run; T-INT-02, 03, 05 in the editor pass.

— §4.9, `source/gdd.md` line 2800, beside §4.11's row-9 cell, which daggers
`T-INT-02` and `T-INT-05` and not `T-INT-03`. The † bullet at 2979–2986 states
both halves outright and gives the reason:

> **T-INT-03 stays unmarked on the rule, not on cost:** §4.9 does place it in
> the editor pass, but what it asserts — an illegal command leaves the state
> hash unchanged and returns a reason, no partial application — is the bridge
> behaviour §4.9 contracts ("an invalid command returns a rejection reason and
> changes nothing"), and a marked ID may not guard a rules invariant. The
> consequence is stated rather than hidden: an editor pass cut to its marked IDs
> alone would still owe T-INT-03, so this line thins that pass, it never cancels
> it.

So the master asserts, in one place and without hedging, that `T-INT-03` is in
the editor pass **and** is unmarked. The dagger and the venue are different
predicates — cut-line membership, versus where an ID runs — and §4.5's rule that
the build-order table is "authoritative for which side an ID is on" governs the
first only; §4.9 is not competing with it. A defect would require some sentence
equating dagger-membership with editor-pass membership, and none does: the †
bullet denies that equivalence by name and discharges its consequence. The
discrepancy as originally filed rests on that unstated equivalence, which is why
run `-1` found the bullet "dissolves much of the discrepancy it files and flatly
denies the conclusion it draws," and why the author's deletion of the change
request was correct. The draft's own check-results bullet states the master's
position accurately — *"the two passages never disagreed"* — so the section was
right and the escalation was the outlier. No violation arises and there is no
Director item here for a later round.
