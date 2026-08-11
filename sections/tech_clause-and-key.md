# Technical design — clause-and-key addendum (tech-director)

## Placement
Pair 1 edits §3 (the parenthetical after the provenance-ledger table); Pair 2 edits §4 (the `GATE-DATA-VENDOR` manifest passage).

## Draft

### Pair 1
**OLD**
```
so every commit link this section carried then resolves; each commit cited since is pinned at the landing that cites it, and the §3 status line above carries that pinning.
```
**NEW**
```
so every commit link this section carried then resolves.
```
Note: the deleted clause quantified over "each commit cited since" — a set that grows with the next citation, so no commit encloses it. What remains is the sentence's own measurement, whose set is fixed at the named commit `ec15be6` that the same sentence cites. The boundary is the semicolon, which is where the sentence stops speaking about that fixed set.

### Pair 2
**OLD**
```
so a `dataCommit` behind the crew commit this
document stands at is the **expected** state and not a stale one.
```
**NEW**
```
so a `dataCommit` behind the `rulesCommit`
that `Source/StratRules/StratRules.manifest.json` records at the same UE
project commit is the **expected** state of `Data/StratData.manifest.json` and
not a stale one.
```
Note: the comparator named neither the file it reads nor the key in it, and the UE tree records two keys — `dataCommit` and `rulesCommit` — at every commit. Both sides are now named as §3 names them: `dataCommit` in `Data/StratData.manifest.json` and `rulesCommit` in `Source/StratRules/StratRules.manifest.json`. Naming the file `dataCommit` is read from also fixes which *state* is meant — a recorded manifest field, not game state.

## Change requests
None.

## Open questions for the Director

1. **`That form` does not refer to the deleted clause, and no pair here repairs it.** The master reads against that referent at each point the sentence gives one. The ruling is said to be "confined to this sentence" rather than to a clause. What it declined to generalise is "restating every reachability claim in this document **against a named commit**", which describes the ancestry measurement in the first half of the sentence and not a pinning-at-landings rule. The same parenthetical later calls the identical move "Ruling S's move applied to the other half" while replacing head-reachability with a named sha. And the form is said to "match the §3 status line above", which carries ancestry at a named commit. If the Director reads the referent the other way, Pair 1 should be held rather than merged, because on that reading it strands a referent this addendum does not repair.
2. **Which `dataCommit`–`rulesCommit` orderings are expected, and which are stale?** The sentence Pair 2 edits rules only on a `dataCommit` *behind* the comparator. It says nothing about a `dataCommit` ahead of that `rulesCommit`, which is the ordering both worked examples in that same passage exhibit, so the passage states a rule and then illustrates a case the rule does not reach. The rule for the ahead ordering — and whether "stale" is an ancestry question at all, rather than a question of whether an unvendored data-touching crew commit exists — is yours to write; I will write the gate for it.
3. **Pair 2 and the pending `stamp-scope` Pair 2 have the same `OLD`, so at most one can apply.** Applying either removes the other's anchor. Pair 2 here carries what the pending pair achieved — the referent "the crew commit this document stands at" is gone either way — and additionally names the key. Choosing between them is a merge decision and I have not made it.

## Grounding

- Pair 1 `OLD` is byte-exact from `source/gdd.md` and unique: the full escaped string, matched newline-sensitively, returns a count of 1 document-wide.
- Pair 1 `OLD` sits in §3: the nearest preceding `## ` heading is `## 3. AI Architecture — how AI agents are used (roles)`.
- The clause Pair 1 deletes and its enclosing sentence are one line in the hard-wrapped master, so a line-oriented match sees the whole span; the substring `landing that cites` returns a count of 1 document-wide, so the clause has no second site.
- Pair 1 `OLD` does not overlap any `OLD` of the gated-unmerged `sections/tech_stamp-scope.md`: that file's Pair 1 anchor `This draft stands at` and its Pair 3 anchor `whose substance is unchanged` both return a count of 1 document-wide and neither falls inside Pair 1's span here. **Pair 1's `OLD` therefore still matches whether `stamp-scope` is merged first or second.**
- Pair 2 `OLD` is byte-exact including its line break and unique: the two-line string, matched newline-sensitively, returns a count of 1 document-wide, and the substring `document stands at` returns a count of 1.
- Pair 2 `OLD` sits in §4: the nearest preceding `## ` heading is `## 4. Technical Strategy`.
- Pair 2 `OLD` is byte-identical to the `OLD` of Pair 2 in `sections/tech_stamp-scope.md`. **It matches only if this addendum is merged before that one; it does not match if that one is merged first.** The reverse holds for that pair against this one.
- Both keys and both file paths in Pair 2's `NEW` are already stated together in §3, which reads ``dataCommit` … in `Data/StratData.manifest.json` and `rulesCommit` `cb8e12b` in `Source/StratRules/StratRules.manifest.json``.
- `Data/StratData.manifest.json` also occurs in §4, so Pair 2's `NEW` introduces no path §4 does not already carry.
- The ahead ordering cited in Open question 2 is F4 of `source/FACTS_clause-and-key.md`, measured per sha with `git merge-base --is-ancestor` against the recorded keys F3 read from the UE project repo at each of the passage's two worked-example commits.
- The substring `stands at` returns a count of 2 document-wide, at the §3 status line and at Pair 2's site; Pair 2 removes the §4 one, and the §3 one is the pending `stamp-scope` Pair 1's own anchor, which this addendum does not touch.
- `sections/tech_stamp-scope.md` is sealed against its accept record and is not edited here. Its Open question 2 quotes the clause Pair 1 deletes and its Pair 2 shares Pair 2's anchor here; both are out of reach for that reason, and Open question 3 above is where the consequence is reported instead.
