# Gate report — run `row10a-3`

- Master: `source/gdd.md`, MANIFEST md5 `afb16df47373ddcd2f23bd8b15102b7e` (unchanged
  across all three runs; the master has not moved under this draft).
- `source/MANIFEST.txt` present; all three source files listed. No `sync-missing`.
- Sections read: `sections/tech_row10a-save-format.md` (16 pairs), diffed against the
  version gated at `row10a-2`.
- Top-level verdict: **PASS**. Zero violations.
- **Nothing is escalated beside this verdict.** There is no non-blocking observation
  outstanding, and no finding held back from the violation list.

---

## `sections/tech_row10a-save-format.md` — PASS (0 violations)

Both defects are cleared, and the three edits introduce nothing new.

### 1. The `row10a-2` violation is cleared

**Filed then:** `invented-fact`, on change request 1's *"Both survive this round on the
measurement"* — a UE-repo measurement that had not been made.

**Now:** the request does not retreat to the crew half, and it does not repeat the
attribution. It states which durable equivalent exists for each half, that the two were
established separately, and — the load-bearing sentence — that **neither is the claim
the parenthetical makes**:

> **Neither of those measurements is the claim the parenthetical makes.** No
> branch-head reading was taken for either repo, on purpose: reachability from a head
> and reachability from a sha are different assertions, and it is the first that
> expired inside an hour and produced the defect Pair 1 repairs.

Checked claim by claim against the master and the round's measurements:

- The quotation of the parenthetical is exact against `source/gdd.md` §3 — both the
  crew-repo *"reachable from the head of `main`"* half and the *"`99fcb84` and
  `9dec48c` … each reachable from the head of `master`"* half.
- The crew-side durable equivalent is what Pair 1 carries and what the round measured:
  `d837fc8` an ancestor of `737f666`, 13 of 13 cited crew commits reachable from
  `737f666`.
- The UE-side durable equivalent — `99fcb84` an ancestor of `9dec48c`, both reachable
  from `9dec48c` — matches the Director's measurement as supplied, and is attributed to
  the Director in Grounding rather than absorbed as the author's.
- *"it is the first that expired inside an hour"* is accurate: the fact block records
  the `git ls-remote` head reading as *"true when gated and false within the hour"*.
- The conclusion is unchanged and remains correct — no pair touches the parenthetical.

**The distinction from what I filed.** The rejected text attributed the parenthetical's
survival *to* a measurement that did not exist and disclosed no gap. The new text
separates the truth of the sentence from the measurements taken and states plainly that
the measurements are not the sentence's claim. Its one truth assertion is explicitly
as-of qualified — *"the parenthetical is true as this draft stands"* — and the paragraph
that carries it names exactly what was and was not checked, so the Director cannot be
misled about the basis. That is a sound disclosure, not an unsupported claim, and I do
not file it.

### 2. The staled Pair 1 clause is gone, and its deletion is clean

*"no ancestry was measured for it this round"* was made false by the measurement taken
after it was written, and would have merged as a false sentence. Pair 1's UE clause now
reads:

> `9dec48c` is cited as a commit, and this line makes no claim about how it stands to
> any branch.

- **This is a statement about the line, not about the world**, so no later measurement
  or push can stale it. That is the durable form.
- **It is true of the line.** The status line names `9dec48c` by sha only; the crew
  half's *"rather than read off a branch"* is a statement of method about `737f666`, not
  a branch claim about `9dec48c`; and the historical sentence reports what the line
  *previously* said. Nothing in Pair 1 asserts how `9dec48c` stands to any branch.
- **It still does not collide with §3's surviving parenthetical**, which does make a
  head-phrased claim about `9dec48c` — because Pair 1's sentence is scoped to itself by
  its own words.
- The new UE measurement was correctly **not** folded into Pair 1. Had it been, the
  master would carry a second sha-anchored ancestry claim that no pair's reasoning needs
  and that the Director has not yet ruled on. Keeping it in the change request is the
  right place for it.

### 3. The rewritten grounding bullet, judged on its merits

> Pair 1 asserts no ancestry for `9dec48c`, and its UE-repo clause is confined to citing
> the commit.

This is the correct repair and not merely a smaller one. The old bullet grounded a
clause that no longer exists *and* carried the same expiry defect, being a claim about
what had been measured. The replacement is a claim about what the pair *says*, which is
checkable against the pair and cannot be falsified by anything measured later. I confirm
it is accurate against Pair 1 as written. The added bullet attributing the UE ancestry
measurement to the Director, with its two commands and its timing *"after Pair 1 was
gated"*, is accurate and correctly attributed.

Flagging the edit as outside the change-scope instruction rather than burying it was the
right call, and I endorse it on the gate's own terms: a scope rule is not a reason to
merge a sentence known to be false.

---

## No new expiring claim, and no new universal

I swept the whole file rather than the edited regions, since that is what was asked.

**Universals** — every one is measured and sha-anchored:

- Pair 1's *"every crew-repo commit this GDD cites is reachable from `737f666`"* —
  measured 13 of 13 per sha, and anchored to a commit rather than a head.
- Pair 3's *"Every other row's tally is unchanged from the pre-change baseline, under
  both compilers"* — measured, and scoped to the landing.
- Pair 3's *"No in-editor harness is among the thirteen `main()` definitions above"* —
  verified at `row10a-2` on the master's own evidence, scoped to `737f666`.
- Pair 7's *"the closure convention this document states once, here"* — verified: after
  Pairs 5, 15 and 16 the full conditional occurs at exactly one site.
- Pair 11's *"nothing re-dates on its account"* — verified against the master.
- Change request 1's *"No branch-head reading was taken for either repo"* — a negative
  about what this round did, which no later event can falsify.

**Expiring claims** — none introduced. The clause that staled is deleted and nothing
replaces it. Every present-tense claim that remains is either sha-scoped (*"at
`737f666`"*, *"at this commit"*), a statement about the document's own text, or one of
the master's existing standing conventions carried forward unchanged — *"`g++` is still
not installed on this machine"* appears at seven earlier landings in §3, and *"This hash
is still unbuilt"* is the register §4.10 already uses. The one temporal assertion added
this round carries its own as-of qualifier.

I also re-checked the Check-results bullet on the reachability parenthetical, which was
**not** edited: *"it survives the push on the measurement"* refers to the crew push and
the crew measurement, and *"Pair 1 is … asserting nothing about the UE project commit's
relation to a branch"* is still true of the rewritten Pair 1. The edits did not stale it.

---

## What changed, verified rather than accepted

Three changes, all outside the pair OLD blocks, exactly as described: Pair 1's **NEW**
block, change request 1, and the Grounding bullets (one rewritten, one added). I diffed
the file against the `row10a-2` version in full. **All 16 OLD blocks are
byte-identical**, so the anchor set has not moved. Fifteen of the sixteen NEW blocks are
byte-identical; only Pair 1's differs, and only by the deletion described. Every pair
heading, every descriptor line, the Arithmetic section and the Check-results section are
unchanged. 16 `**OLD**` markers and 16 `**NEW:**` markers, matching the mechanical
count.

---

## Re-confirmed on this file

- **The figure that must not move has not moved.** §3's *"Eight IDs are still recorded
  as **uncovered**"* — T-MOVE-07 and T-SCN-10 unwritten; T-DATA-05, T-SCN-08, T-SCN-09,
  T-SCN-11, T-UI-03, T-UI-04 written and not green — is untouched by every pair, and the
  Arithmetic bullet reproduces it correctly. `T-SAVE-04` was never among the eight.
- **§4.5's arithmetic.** Decomposition 18+9+9+6+7+1+2+1+1+1 = 55, plus Pair 7's new `1`
  at `737f666` = 56 (Pair 6). Unclosed: 1 + 3 + 2 + 3 + 6 = 15 (Pair 8), against the
  pre-change 1 + 3 + 2 + 3 + 7 = 16. Written stays **71** — no ID minted,
  `GATE-SAVE-PARSE` mints none. **9** verified ledger rows and §3's *"Nine rows carry a
  ✓"* untouched.
- **The `main()` series.** 12 → 13 at `737f666`, 11 harnesses + 1 duel simulator + 1
  REPL, consistent with §3's own decomposition of the twelve at `7c36303`.
- **All three "row 10 holds no code" sites** moved (Pairs 2, 9, 13), every neighbouring
  canonical-state-hash clause surviving and still true.
- **Rulings K, L, M and N** unchanged and re-verified: the closure convention stated at
  exactly one site, `T-INT-01` at `d837fc8` and `T-INT-04` at `b23823f` throughout, no
  green re-dated, §4.9's ten-module enumeration byte-identical.
- **No `kb-desync`** — nothing in §2 moves. **No `placement-collision`** — one section,
  16 distinct anchors. Insertions by substring test are 4, 11, 12 and 14, matching the
  Arithmetic section's statement.

---

## Verdict

**PASS.** `sections/tech_row10a-save-format.md` carries zero violations and is clear to
merge at the placement each of its sixteen pairs specifies. Both defects are properly
closed rather than papered over: change request 1 now tells the Director what was
measured, what was not, and that neither measurement is the claim the parenthetical
makes — which is a better request than the one I blocked, because it makes the Director's
actual question visible; and Pair 1's staled clause is deleted rather than patched, with
the new measurement deliberately left out of the master where it has not been ruled on.
I swept the whole file for new universals and new expiring claims and found none: every
universal is measured and sha-anchored, and the only temporal assertion added carries its
own as-of qualifier. The arithmetic holds on every figure — 71 / 55 / 16 → 71 / 56 / 15,
the decomposition's `+1` at `737f666`, `main()` 12 → 13, nine verified ledger rows — and
the eight-uncovered figure is untouched by every pair, which is correct. **Nothing is
escalated beside this verdict**; the `main()` observation raised at `row10a-1` was closed
by the `row10a-2` correction and no new observation replaces it. The Director may merge.
