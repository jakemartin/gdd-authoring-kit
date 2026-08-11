# Gate report — run `clause-and-key`, third pass

**Top-level verdict: PASS.**

| File | Verdict | Violations |
|---|---|---|
| `sections/tech_clause-and-key.md` | **PASS** | 0 |
| `source/FACTS_clause-and-key.md` | **PASS** | 0 |

`source/MANIFEST.txt` is present and records `gdd.md` at md5
`1f27e981b623c7af2f6402d9a5b6a62b` — the same md5 the first and second passes
measured against. Every line number below was measured today by reading or
matching against the named file; attributions to a GDD section are by nearest
preceding `## ` heading and no finer, the heading lines being 1425
(`## 3. AI Architecture — how AI agents are used (roles)`) and 1544
(`## 4. Technical Strategy`), measured with a `^## ` match over
`source/gdd.md`.

---

## `source/FACTS_clause-and-key.md` — PASS (the second pass's one violation is cleared)

### 1. The deletion is complete

The second pass filed the closing clause of F2's correction. The sentence then
read:

> The body below is left standing, including its instruction to test the
> inference rather than adopt it, **because that instruction is what caused the
> error to be caught.**

It now reads, in full, at line 81 of `source/FACTS_clause-and-key.md`, measured
by reading that file today:

> **Consequence: Pair 1 strands nothing, and this round has no stranded-referent
> pair.** The body below is left standing.

More was removed than the fix prescribed — the fix said to end the sentence
after `rather than adopt it`, and the trailing participial phrase went with the
clause. That is not a finding: what remains states the negative and stops, and
nothing that was load-bearing was carried by the removed phrase. The body it
refers to still carries the instruction on its own, at lines 88–90 of the same
file: `**INFERRED:** that \`That form\` refers to the clause being deleted …
**may not be promoted to a bare assertion.** If you find it refers to something
else, say so and stop — that changes the round.`

**The attributed cause is gone from the whole file, not relocated.** The file
was matched end-to-end for `caught`, `instruction`, `credit` and `is what`:
zero hits for all four. `because` returns two hits, at lines 92 and 122, and
neither attributes the catching of an error to any instruction — line 92 is the
blast-radius sentence (`scope is what your edits make false, not what the round
is about`) and line 122 is F4's declared reading (`this does not falsify the
sentence, because the sentence is conditional`). Both predate the correction and
neither is a positive volunteered beside a negative finding. No restatement of
the attributed cause under other words was found anywhere in the file.

### 2. The correction survives the deletion on all four cleared points

**a. The right defect is still named.** Lines 62–67 are untouched: the heading
is faulted for stating the conclusion *"deleting it strands a referent"* as the
fact's title and for labelling the fact MEASURED, `promoting the exact step the
body below forbids promoting`. That is the defect the first pass filed.

**b. The false inference is still correctly declared false, and it is still
false.** Re-measured from `source/gdd.md` at the manifest md5, not carried
forward:

- `That form` returns exactly one match, on line 1533 (§3), and it opens the
  sentence immediately after the clause Pair 1 deletes.
- The §3 status line the sentence says the form *matches* is line 1533's
  referent, and the string
  `` are each an ancestor of `031ee20`, measured with `git merge-base --is-ancestor` per sha ``
  returns exactly one match, on line 1516 (§3) — presence and attribution both
  hold, checked separately.
- The pinning language is not on that status line. `landing that cites`,
  `pinned at the landing` and `carries that pinning` together match one line
  document-wide, and that line is 1533, not 1516. So the status line carries the
  ancestry form and carries no pinning-at-landings statement, which is what the
  correction says.
- `restating every reachability claim in this document against a named commit`
  is on line 1533 as the generalisation the ruling declined, matched twice on
  that one line — once beside `the ruling is confined to this sentence` and once
  beside `Ruling S was made and declined, and that declining stands`.
- `Ruling S's move applied to the other half` is on line 1533, in the same
  parenthetical, immediately after `The claim this replaces was that each is
  reachable from the head of \`master\`; a head expires and a sha does not` —
  i.e. beside the replacement of head-reachability with a named sha, as the
  correction states.

**c. The three measurements are still attributed as the gate made them.** The
three bullets of the correction (lines 71–78) map one-to-one onto the three
re-measurements above, in the same order and with the same content, and the
deletion removed none of them and altered none of their wording.

**d. The marked-in-place heading is still not readable as current.** The
correction is still the first thing under the F2 heading at line 58, is bolded,
and says in its own opening that `This heading is the defect, and its inference
is false.` The deleted clause was the last sentence of the correction and
carried none of that marking, so its removal does not move the mark closer to
the body or further from the heading.

---

## `sections/tech_clause-and-key.md` — PASS, confirmed unmodified

**Confirmed rather than assumed, with one discrepancy recorded.** No hashing
tool is available to this gate, so the file was re-read in full today and
matched against every quotation and structural claim the second pass's report
recorded of it. Pair 1's `OLD`/`NEW`, Pair 2's `OLD` at draft lines 22–23 and
`NEW` at 27–30, the two Notes, `Change requests: None`, and all three Open
questions are present in the same order and wording. Both anchors were re-run
against the master today: Pair 1's `OLD` returns exactly one match, on line 1533
of `source/gdd.md` (§3), and Pair 2's `OLD` returns exactly one match, spanning
lines 2706–2707 (§4), matched newline-sensitively across the line break.

The discrepancy: the Grounding section carries **12** bullets, measured today
with a line-anchored `^- ` match over `sections/tech_clause-and-key.md`, at
lines 45–56. The second pass's report said thirteen. I cannot distinguish a
miscount in that report from a deletion, and I do not claim which it was. What I
did measure is that nothing in the draft is left ungrounded by the 12 present:
both `OLD`s' uniqueness and section, the clause's absence of a second site, the
non-overlap with `stamp-scope`'s Pair 1 and Pair 3, the shared Pair 2 anchor and
its merge-order consequence, the provenance of both keys and both file paths,
the `stands at` count, F4's attribution, and the seal on
`sections/tech_stamp-scope.md` are each carried by a bullet. No claim in the
draft is unsupported, so nothing is filed, and the section's PASS stands.

### Carried forward as context: the merge-order dependency (not a violation)

Recorded again so the Director has it in the current record. Pair 2's `OLD`
here is byte-identical to the `OLD` of Pair 2 in the sealed, gated-unmerged
`sections/tech_stamp-scope.md`, and the master carries that string once,
spanning lines 2706–2707 of `source/gdd.md` (§4 by the heading at line 1544),
measured today. **At most one of the two can apply**; whichever merges first
removes the other's anchor. This draft's Pair 2 is the one that names the key.
Pair 1 carries no such dependency: its own anchor at line 1533 does not contain
`stamp-scope`'s Pair 1 or Pair 3 anchors, so it matches whether `stamp-scope`
merges first or second. This is a merge-order decision for the Director, filed
as such by the author in Open question 3 and in Grounding; it is not a defect in
either file, and nothing is filed against `sections/tech_stamp-scope.md`, which
is sealed.

---

## Verdict

The run is **PASS**, with zero violations in either file. The clause filed on
the second pass is gone from `source/FACTS_clause-and-key.md`, and it was not
relocated or restated in other words anywhere in that file; the correction it
sat in survives intact on the four points the second pass cleared it on, each
re-measured today against `source/gdd.md` at the manifest md5 rather than
carried forward. `sections/tech_clause-and-key.md` is unmodified on every
quotation and structural claim previously recorded of it, both its anchors still
match the master exactly once each, and it remains **PASS** with zero
violations, so it is merge-eligible on this accept record. Before it merges the
Director must sequence it against the sealed `sections/tech_stamp-scope.md`: the
two Pair 2s share one anchor, applying either destroys the other's, and this
draft's Pair 2 is the one that names the key — that ordering is the only thing
still standing between this draft and the master.
