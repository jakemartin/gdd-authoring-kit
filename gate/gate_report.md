# Gate report — run `fixture-widened-2`

`source/MANIFEST.txt` present. `gdd.md` md5 `1bfae9f169230f3bdcea4fab48b100f8`,
matching the md5 the draft's Placement heading declares.

Sections read this run: `sections/tech_fixture-widened.md` (one file, as scoped).

**Top-level verdict: PASS. One section, PASS, 0 violations.**

---

## `sections/tech_fixture-widened.md` — PASS (0 violations)

No violation is filed. What follows records what was checked and how, because a
PASS on a round whose previous run blocked is only worth the derivation behind it.

### 1. The §4.8 / §4.9 boundary, re-derived rather than deferred to

Measured on `source/gdd.md`, not carried over from run `fixture-widened-1`:

- `### 4.8 Data contract — DataTable schemas` — line **2669**
- `### 4.9 Headless-module → Unreal integration path` — line **2772**

So §4.8 spans 2669–2771 and §4.9 begins at 2772. The draft's Pair 11 anchor
states exactly that and pins its OLD at 2686–2689, which is inside §4.8. Verified.

All six moved citations check out against that boundary:

| Site | Draft text | Derived location | Verdict |
|---|---|---|---|
| Placement list | "§4.8 (the `dataCommit` ruling)" | 2682–2689 | correct |
| Placement list | "§4.9 (part 2's `0897cb5` vendoring paragraph)" | 2967–2968 | correct — §4.9 begins 2772 |
| Sweep paragraph | "the illustrative clause after §4.8's `dataCommit` ruling" | 2686–2689 | correct |
| Disposition row 32 | "§4.8's 2026-08-06 ruling … also in §4.8" | 2682–2689 | correct, both instances |
| Open Question 4 | "What should §4.8's `dataCommit` illustration point at?" | 2686–2689 | correct |
| Grounding, OQ 4 | "the master's §4.8 clause and §3 record" | 2686–2689; §3 at line 1516 | correct — the sixth site, self-reported and not in run 1's list |

The author's assertion that Pair 8's anchor at 2967–2968 is genuinely §4.9, and
that both sections therefore belong in the Placement list rather than one
replacing the other, is confirmed. The sub-locator "part 2" is a description of
the paragraph's own stated subject — the paragraph opens "**No further spec-stub
pass is owed for part 2 (ruled 2026-08-05).**" and reports part 2's bridge
landing at `0897cb5` — and the OLD is a unique literal match, so the placement
merges mechanically. Not filed.

`dataCommit` occurs at exactly four sites in the master (1516, 2682, 2685, 2690);
only 2686–2689 states a value in the present tense, and Pair 11 is the only pair
that touches it. No fifth site was left behind.

### 2. Pair 4 — the extended OLD, the highest-risk edit in the round

**Unique literal match.** The extended OLD runs from "**`Build` can be produced,
and this fixture's harness never asks for it:**" through "…is below the cost."
Measured on the master: the join "before Fame is consulted; `Balance`'s
equivalent view does assign a buildlist. Fame sufficiency is not what stops it"
occurs **once**, and "is below the cost." occurs **once**. The extension is a
unique literal match and can be applied without ambiguity.

**The three standing data facts are not put into the past.** Verified verbatim
in the NEW: "`startingFame` **is** 200 a side, Infantry's `CostFame` **is** 100,
side 0 **owns** the `Factory` hex at column 1 row 4 with `IsSpawnPoint` true, and
`queueBuild` **refuses** only when `fameTotal` is below the cost." All four
clauses remain finite present tense, which is what the fact block's §9 requires
of the first three. The only verb moved is the one §9 names — "is not what stops
it" → "was not what stopped it" — plus "the harness builds" → "`aiViewOf` built"
inside the same pair's opening clause, which is pinned to `0897cb5` in the NEW's
own subject ("the harness that emitted the fixture replayed at `0897cb5`").

**The relocated `c2f5860` clause strands nothing.** The passage now runs
past-cause → standing data facts → present state: "…`queueBuild` refuses only
when `fameTotal` is below the cost. At `c2f5860` `aiViewOf` supplies `Infantry`,
looked up by `Id`, and the fixture carries `Build`." The final clause introduces
no presupposition of its own and no clause after it depends on one. The retained
present-tense contrast "`Balance`'s equivalent view does assign a buildlist"
stands against the past-tense clause immediately before it and remains true of
`Balance` at every commit in play.

**Disposition row 26 discloses the edit** rather than claiming the sentence is
untouched — "unchanged and still true, but re-tensed inside Pair 4" — which is
what makes the fact block's "unchanged" and the draft's treatment consistent
rather than in conflict.

**Record of authority.** This repair was invited by the orchestrator, not
freelanced by the author: fact block §9, added after run `fixture-widened-1`,
records that the §3 claim "the master's statement to that effect is unchanged"
was the orchestrator's call, was not a measurement, and was overruled by the
author with reason. Nothing here is filed against the text; had it been, the
finding would have named the instruction as the orchestrator's.

### 3. Antecedents — the species run 1 named at one site

Every pair's NEW was read for a pronoun, a bare "there", or a definite article
whose nearest antecedent in the master is `fed8ae9` or `cb8e12b` rather than
`0897cb5`.

- **Pair 5** — the filed site. NEW reads "none having run since the one at
  `0897cb5`", and the second clause, which run 1 did not name, now reads "the
  fixture **that pass** replayed did not carry them". "That pass" is bound to
  "the one at `0897cb5`" named immediately before, and the binding is forced
  semantically as well as by proximity: a pass that has not run cannot have
  replayed a fixture. Repaired.
- **Pair 8** — the unfiled site. The master's "that commit" (nearest token
  `cb8e12b`) is gone; the NEW pins with "none having run since the one at
  `0897cb5`" and "vendored into the UE project at `4ceaf93`". Repaired.
- **Pairs 1, 2, 6, 7, 10, 11** — each carries an explicit `0897cb5`, `c2f5860`
  or `4ceaf93` at the point where the master left the reference bare. No bare
  "there" or "that commit" survives in any NEW.
- **Pair 9** carries "the parity fixture replayed there", inherited byte-for-byte
  from the OLD and not introduced by this draft; the tense change to "carried"
  is true under either available reading of "there". Not a violation of this draft.
- **Pair 2**'s "the two commands **it** had lacked" resumes the clause chain's
  subject, "The committed fixture"; the intervening "the UE project at `4ceaf93`"
  is not a thing that can lack commands. Unambiguous. Not filed.

Sweep for completeness: "a parity fixture carrying the complete §4.9 command
set" occurs at six sites in the master (§3 line 1516, §4.4 line 1569, §4.5 line
1589 twice, §4.9 line 2968, §4.11 line 3249). All six are pairs — 2, 5, 6, 7, 8,
10. No seventh site was left unamended.

### 4. Everything else checked

- **Anchors.** All eleven OLDs are unique literal matches against
  `source/gdd.md`, including the two that span hard line wraps (Pairs 8 and 11),
  checked newline-insensitively. No NEW contains its own OLD; none of the eleven
  is an insertion, as the draft states.
- **Numbers.** No pair closes an acceptance ID, flips a §3 ledger row, or moves
  71 / 62 / 9, row 9's 3 or row 10's 1. Pairs 6 and 7 sit inside §4.5's "9 IDs
  remain unclosed" sentence and leave every figure in it standing; Pairs 2, 5, 6,
  7, 8 and 10 all preserve "without closing" or its equivalent and all state
  "none having run since `0897cb5`". `kParityTurns`, the byte and command counts
  and the two `stateHash` values appear nowhere in the master, and the draft
  states them only inside Open Question 2, which is the correct disposal.
- **Grounding.** Every substantive claim in the eleven pairs traces to the fact
  block: Pair 3's `appendAiTurn` / `Ai.h` / §4.10 `unit` field claims to §3;
  Pair 11's `862a225` → `c2f5860` and the CSVs' byte-identity across the two
  vendorings to §4; the "no editor pass since `0897cb5`" claims to §5, first
  bullet. `§3` of the master independently records `dataCommit` `862a225` at
  `0897cb5` ("The UE tree there records `dataCommit` [`862a225`] …", where
  "there" is `0897cb5`), which is what Pair 11's NEW pins against.
- **Unverified claims.** The draft claims no gate run. `GATE-DATA-VENDOR`, which
  fact block §5 records as **not run**, is asserted nowhere in any pair.
- **Scope.** All eleven pairs land in §3, §4.4, §4.5, §4.8, §4.9 and §4.11 — the
  tech-director's lane. No §2 text moves, so `kb_rules.md` is not put wrong by
  this draft and no `kb-desync` arises.
- **Placement collisions.** One section this run; the Placement list names all
  six sections the eleven pairs touch, and every placement resolves to a unique
  literal anchor.
- **Format.** Placement, Draft, Change requests, Open questions, Grounding all
  present.
- **Voice.** Declarative, present tense except where a clause is deliberately
  pinned to a past run, which is this round's whole subject. No UI strings.

---

## Verdict

**PASS.** `sections/tech_fixture-widened.md` clears the gate with zero
violations: both of run `fixture-widened-1`'s findings are repaired at every
site, including the sixth `dead-reference` site and the two further antecedent
sites the gate did not name, and the §4.8/§4.9 boundary, all six moved
citations, all eleven OLD anchors and the extended Pair 4 OLD were re-derived
against `source/gdd.md` rather than taken on report. Nothing must happen before
merge beyond the Director's ordinary merge checklist: apply the eleven old→new
pairs at their stated placements, rebuild the `.pdf` and `.txt`, and re-run
`python sync.py`. `kb/rules.md` needs no re-parse on this draft's account, since
no §2 text moves. Five open questions go to the Director unanswered and none of
them blocks the merge — Open Question 4 in particular asks what §4.8's
`dataCommit` illustration should point at now that Pair 11 replaces the worked
example with a pinned pair of vendorings, and wants a Director-named commit if
the worked example is to survive.
