# FACTS — round `clause-and-key`

**Subject.** Two Director rulings, both against §3/§4 apparatus prose: delete a
clause that asserts a universal over an open-ended set, and name the manifest key
a comparator leaves underdetermined.

## Pre-send pass — run, not declared

Each fact below was re-measured in the unit the author will use it in. No fact is
written "at `<sha>`" bare. Material facts are separated from my justification.
Each fact is labelled MEASURED or INFERRED, and **an INFERRED fact may not be
promoted to a bare assertion.**

Each quotation was checked for **three** claims, not two: that the string exists,
that it exists where attributed, **and that any number attached to it is a count
of the string as quoted.** The third was added after gate run `stamp-scope` filed
a count of 8 against a quotation whose string occurs 6 times — the pass had been
declared complete without being run.

All measurements are against `source/gdd.md` md5
`1f27e981b623c7af2f6402d9a5b6a62b`, 3366 lines, byte-identical to the master at
sync time. String work is on a whitespace-collapsed copy. Each matcher was
control-tested against a mutated copy of its own target (0 hits).

## F0 — READ THIS FIRST: an unmerged addendum edits the same parenthetical. MEASURED

`sections/tech_stamp-scope.md` is gated **PASS** at run `stamp-scope` and is
**not merged**. Its three `OLD` strings are all still present in the master,
count **1** each:

| Pending pair | Its OLD, in the master today |
|---|---|
| Pair 1 | `This draft stands at 2026-08-06, at commit …` (§3) |
| Pair 2 | `document stands at` (§4) |
| Pair 3 | `it matches the §3 status line above, whose substance is unchanged` (§3) |

**Pending Pair 3 edits the sentence immediately after the clause this round
deletes, inside the same parenthetical.** Your pairs must not collide with any of
the three, and you must state your round's ordering dependency on them — whether
your `OLD` strings still match if `stamp-scope` is merged first, and whether they
still match if it is merged second. **Do not edit `sections/tech_stamp-scope.md`;
it is sealed against its accept record.**

## F1 — the clause to delete. MEASURED

Occurs **once** document-wide, on line 1533, in §3 by nearest preceding `## `
heading:

> each commit cited since is pinned at the landing that cites it, and the §3 status line above carries that pinning.

Ruled for deletion by the Director on 2026-08-11. The reasoning is in
`RULING_ledger-reading-point.md`: as a measurement it is a universal over an
open-ended set and expires on the next citation; as a rule it needs a gate that
would have to enumerate acceptable phrasings, which this project wrote once and
withdrew. **The exact deletion boundary — what punctuation and joining words go
with it — is yours to determine and must be byte-exact.**

## F2 — deleting it strands a referent. MEASURED, with one INFERRED step

> **Corrected 2026-08-11, gate run `clause-and-key`, marked beside the claim
> rather than over it. This heading is the defect, and its inference is false.**
>
> **The heading is wrong twice.** It states the conclusion *"deleting it strands a
> referent"* as the fact's title, and labels the fact MEASURED — promoting the
> exact step the body below forbids promoting. A heading is a claim. The label
> belongs to what the heading asserts, not only to the sentences under it.
>
> **The inference it promoted is also false.** `That form` does not refer to the
> clause being deleted. It refers to the ancestry-against-a-named-commit
> measurement in the first half of the same sentence. The author tested it and
> rejected it, and the gate verified the rejection independently from the master
> on three measurements: the §3 status line the sentence says the form *matches*
> carries `are each an ancestor of \`031ee20\`, measured with \`git merge-base
> --is-ancestor\` per sha` and carries no pinning-at-landings statement at all;
> the ruling's declined generalisation is `restating every reachability claim in
> this document against a named commit`; and the same parenthetical later calls
> that move `Ruling S's move applied to the other half` while replacing
> head-reachability with a named sha.
>
> **Consequence: Pair 1 strands nothing, and this round has no stranded-referent
> pair.** The body below is left standing.

The string `That form` occurs **once** document-wide, and it begins the sentence
**immediately following** the clause: `That form was ruled on 2026-08-05, and the
ruling is confined to this sentence…`.

**MEASURED:** the occurrence count, and that it immediately follows.
**INFERRED:** that `That form` refers to the clause being deleted. That is a
reading of the text and **may not be promoted to a bare assertion.** If you find
it refers to something else, say so and stop — that changes the round.

This is the round's blast radius and it is in scope: **scope is what your edits
make false, not what the round is about.**

## F3 — the manifest keys, for the second ruling. MEASURED

Read directly from the Stratocracy UE project repo at each commit, by
`git show <commit>:<path>`:

| UE commit | `Source/StratRules/StratRules.manifest.json` → `rulesCommit` | `Data/StratData.manifest.json` → `dataCommit` |
|---|---|---|
| `0897cb5` | `cb8e12b3a897c7329497ced4d1c6207630f37101` | `862a225db09437196f5d59691275ffac30db0111` |
| `4ceaf93` | `cb8e12b3a897c7329497ced4d1c6207630f37101` | `c2f58608c77c60c44e6c0fc87988bd3b372beaf5` |

**Both worked examples record the same `rulesCommit`.** The passage therefore
exercises its comparator at two sites and gets one crew commit from both, so the
document does not itself demonstrate the comparator varying.

The defect ruled for repair: **the comparator does not say which recorded key it
means.** The UE tree records two keys at each commit. **That `rulesCommit` is the
one intended is not stated by the master and is not established here** — it is
what the Director is naming, and you should write what they name rather than what
I read.

## F4 — a case the sentence does not cover. MEASURED, with a reading attached

`cb8e12b` is an ancestor of both `862a225` and `c2f5860`, measured per sha with
`git merge-base --is-ancestor` in the crew repo. So at both worked examples
`dataCommit` is **ahead** of `rulesCommit`, not behind.

**The reading, which is mine and is not a fact:** this does not falsify the
sentence, because the sentence is conditional — it explains what a `dataCommit`
*behind* the comparator means, and an ahead case is simply not the case it
addresses. **Check this reading rather than adopting it.** If the sentence does
assert that `dataCommit` is behind, then F4 is a defect and this round's scope is
wrong.

## F5 — not material. My justification, and not for the master

The two rulings came out of measurement I did on the `stamp-scope` round's open
questions 2 and 3. **That history is why this round exists. It is not a fact
about the game or the build and must not be written into the GDD.**

## Disambiguation — the round's own subject nouns

- **clause** — F1's text only. Do not use it for any other span.
- **key** — a named field in a manifest file (`rulesCommit`, `dataCommit`). Not a
  sha, and not the file.
- **comparator** — the thing `dataCommit` is compared *against* in the §4
  sentence. Not the comparison, and not `dataCommit` itself.
- **state** — used in the master for both a repo's commit and the game's runtime
  state. If you write it, say which.

## Forbidden species this round

The round's own subject names the first two. Check your own draft against these
before you return it.

1. **A universal over an open-ended set** — the species being deleted. A
   replacement that quantifies over "each … since" reinstates it.
2. **A comparator that does not name what it reads** — the species being
   repaired. If your prose compares two things, both must be nameable from the
   document or from a file the document identifies.
3. **A claim whose truth depends on a landing, not enclosed by a commit-pinned
   record.**
4. **A closed list offered as sufficient** where only necessity was established.
5. **"at `<sha>`" written bare.** Write *committed at* or *as read at*.
6. **A volunteered positive beside a true negative finding.** State the negative
   negatively and stop.

**This is not a list of approved phrasings and must not become one.** It bans
species; it supplies no vocabulary.

## What is not specified here

**No replacement prose is offered for either site.** The deletion boundary, the
handling of the stranded referent, and the wording that names the key are all
yours — you measure the site and I am working from a brief.
