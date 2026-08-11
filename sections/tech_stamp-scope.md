> # ⚠️ GATED, NOT MERGED — DO NOT RE-GATE
> # ⛔ Pair 2 is SUPERSEDED and MUST NEVER BE APPLIED
>
> This addendum passed gate run `stamp-scope` and **has not been merged**. Do not
> read this banner as an applied mark: **Pairs 1 and 3 are still to be applied.**
>
> **Pair 2 must not be applied.** Its `OLD` is byte-identical to Pair 2 of
> `sections/tech_clause-and-key.md` — md5 `ea28d1ab8e70` over the fenced payload in
> both files — and that string occurs **once** in the master, so applying either
> pair destroys the other's anchor. **The Director ruled on 2026-08-11 to take
> `clause-and-key`'s Pair 2 and drop this one.** That pair removes the same
> referent this one removes, and names the manifest key besides.
>
> Verified 2026-08-11 against `source/gdd.md` md5
> `1f27e981b623c7af2f6402d9a5b6a62b`, 3365 lines by `wc -l`, matched
> newline-sensitively over the fenced payloads: the shared `OLD` occurs once, at
> master lines 2706–2707. Pair 1's `OLD` occurs once, on line 1516; Pair 3's occurs
> once, on line 1533. Neither overlaps the shared span.
>
> **Nothing below this banner was edited.** The pairs, Grounding and Open questions
> stand as gated. Open question 3 of this file asked the Director to make this
> merge choice; it is answered here and not in that section.

# Technical design — stamp-scope addendum (tech-director)

## Placement
Pair 1 edits §3 (the provenance-ledger status line); Pair 2 edits §4 (the
manifest `dataCommit` passage); Pair 3 edits §3 (the reachability-form sentence
after the ledger table).

## Draft

### Pair 1
**OLD**
```
This draft stands at 2026-08-06, at commit [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) in the crew repo and at `fed8ae9` in the Stratocracy UE project repo.
```
**NEW**
```
Recorded here is one dated reading, made 2026-08-06: the crew repo as read at [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) and the Stratocracy UE project repo as read at `fed8ae9`. It dates that reading and nothing else — this status line cites commits made after both of those.
```
Note: the old sentence took *this draft* as its subject and so read as a
reading point for the document. Eleven distinct 7-hex commit tokens in this
status line were measured as non-ancestors of the half naming their own repo,
each committed after it, the earliest on 2026-08-07 and the most recent of the
eleven on 2026-08-10 — so the sentence covered text it does not date. The
replacement records the reading as an event, keeps both shas and the date
auditable, and disclaims the scope rather than asserting a wider one. Both
commits are written *as read at*, not bare.

### Pair 2
**OLD**
```
so a `dataCommit` behind the crew commit this
document stands at is the **expected** state and not a stale one.
```
**NEW**
```
so a `dataCommit` behind the crew repo's
state at the UE project commit the manifest is read at is the
**expected** state and not a stale one.
```
Note: this sentence's comparator was the referent Pair 1 removes — there is no
longer a crew commit *the document stands at*. The manifest the sentence turns
on is the one that records `dataCommit`, which the master places in the UE tree,
and the passage's own two examples read it at UE project commits; so the
comparator is restated against the commit the manifest is read at. The rule the
sentence states is untouched.

### Pair 3
**OLD**
```
it matches the §3 status line above, whose substance is unchanged
```
**NEW**
```
it matches the §3 status line above, whose substance that ruling left unchanged
```
Note: `whose substance is unchanged` is a standing present-tense claim about the
status line, and Pair 1 changes that line's substance. Pinning the clause to the
2026-08-05 ruling it appears in keeps it true across this revision. What the
sentence says it *matches* — the ancestry-at-a-named-commit form — is in the
part of the status line neither pair touches.

## Change requests
None.

## Open questions for the Director

1. **Does the ledger need a reading point at all, and if so what encloses it?**
   Pair 1 disclaims one rather than moving one, because none can be established
   from what was measured: the enumeration behind the eleven late commits sees
   `\b[0-9a-f]{7}\b` tokens only, so it is a floor and not a ceiling, and a
   re-pin to any later pair of shas would assert an enclosure over text the
   probe cannot see. If a reading point is wanted, the rule for establishing one
   — what must be shown to be an ancestor of what, over which set of citations —
   is yours to write, and I will write the gate for it.
2. **Is `each commit cited since is pinned at the landing that cites it` a rule
   or a measurement?** That clause sits in the §3 sentence ending `and the §3
   status line above carries that pinning.`; Pair 3's OLD is in the sentence
   after it, and neither pair edits the clause. Pair 1 leaves it standing and
   does not lean on it. If it is a rule, it needs a gate; if it is a
   measurement, it needs the commit it was measured at.
3. **Pair 2's comparator.** The rule now reads against the UE project commit the
   manifest is read at. Confirm that is the comparison intended, rather than a
   crew-repo reading point restored under another name.

## Grounding

- Pair 1 OLD is byte-exact from `source/gdd.md` and unique: the substring
  `This draft stands at` returns a count of 1 document-wide, and the full
  escaped sentence returns a count of 1.
- Pair 1 OLD sits in §3 by nearest preceding `## ` heading,
  `## 3. AI Architecture — how AI agents are used (roles)`.
- The eleven late commits, their commit timestamps, and the two stamp halves'
  commit timestamps (`c2edae0` committed 2026-08-06T20:02:59-04:00, `fed8ae9`
  committed 2026-08-06T18:58:48-04:00) are F3 of `source/FACTS_stamp-scope.md`,
  measured per sha with `git merge-base --is-ancestor`. The floor/ceiling
  caveat cited in Open question 1 is F3's own **Sufficiency** paragraph.
- Pair 2 OLD is byte-exact including its line break and unique: the substring
  `document stands at` returns a count of 1 document-wide, and the two-line
  string returns a count of 1 under a newline-sensitive match.
- Pair 2 OLD sits in §4 by nearest preceding `## ` heading,
  `## 4. Technical Strategy`.
- The manifest Pair 2 turns on is the one recording `dataCommit`, and it is a UE
  tree file: §3 reads `The UE tree there records `dataCommit` … in
  `Data/StratData.manifest.json``, and §4 reads ``Data/StratData.manifest.json`
  at `4ceaf93` records a sha256 for each of those five names and no others`,
  `4ceaf93` being a UE project commit per F3's UE table. The master distinguishes
  that file from `Source/StratRules/StratRules.manifest.json`, which the same §3
  sentence gives `rulesCommit` rather than `dataCommit`.
- Pair 3 OLD is byte-exact and unique: the substring
  `whose substance is unchanged` returns a count of 1 document-wide, and the
  full clause returns a count of 1.
- Pair 3 OLD sits in §3 by nearest preceding `## ` heading.
- Every count above was taken against `source/gdd.md` md5
  `1f27e981b623c7af2f6402d9a5b6a62b`, the file `source/MANIFEST.txt` records as
  the synced master.
- The §3 clause F5 names — the one whose verb is `are` and whose subject is two
  `T-UI-` acceptance IDs — is not edited by any pair here.
