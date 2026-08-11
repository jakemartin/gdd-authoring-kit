# Gate report — run `stamp-scope`, second pass

Master: `source/gdd.md`, md5 `1f27e981b623c7af2f6402d9a5b6a62b`, per
`source/MANIFEST.txt`. `source/MANIFEST.txt` is present, so the run is not
`sync-missing`. Every count below was taken against that file at that md5.

**Top-level verdict: PASS.** Zero violations.

Out of reach for this round and not filed, as before: the §3 clause F5 names
(verb `are`, subject two `T-UI-` acceptance IDs), and F6.

---

## `sections/tech_stamp-scope.md` — PASS (0 violations)

### Violation 1 (`invented-fact`) — cleared

The Grounding bullet now reads:

> The manifest Pair 2 turns on is the one recording `dataCommit`, and it is a UE
> tree file: §3 reads `The UE tree there records `dataCommit` … in
> `Data/StratData.manifest.json``, and §4 reads ``Data/StratData.manifest.json`
> at `4ceaf93` records a sha256 for each of those five names and no others`,
> `4ceaf93` being a UE project commit per F3's UE table. The master distinguishes
> that file from `Source/StratRules/StratRules.manifest.json`, which the same §3
> sentence gives `rulesCommit` rather than `dataCommit`.

Both quotations were checked for both of their claims — that the string exists,
and that it exists where the draft attributes it.

- The §3 quotation is present, elided only over the commit link, in
  `The UE tree there records `dataCommit` [`862a225`](…) in
  `Data/StratData.manifest.json` and `rulesCommit` `cb8e12b` in
  `Source/StratRules/StratRules.manifest.json``, measured at source/gdd.md line
  1516. Attribution holds: the nearest preceding `## ` heading is
  `## 3. AI Architecture — how AI agents are used (roles)` at line 1425, and the
  next `## ` heading is `## 4. Technical Strategy` at line 1544 — both measured
  by enumerating every `^## ` line in the file.
- The §4 quotation is present across a hard wrap at source/gdd.md lines
  2683–2684 (`… `Data/StratData.manifest.json` at` / ``4ceaf93` records a sha256
  for each of those five names and no others.`), matched newline-insensitively.
  Attribution holds: the last `## ` heading before line 2683 is
  `## 4. Technical Strategy` at line 1544.
- `4ceaf93` is in F3's UE-half table of `source/FACTS_stamp-scope.md`.
- The distinction claim holds: the single §3 sentence at line 1516 gives
  `rulesCommit` to `Source/StratRules/StratRules.manifest.json` and `dataCommit`
  to `Data/StratData.manifest.json`.

The manifest the pair turns on is now grounded on the file the master places in
the UE tree, and Pair 2's comparator is grounded.

### Violation 2 (`dead-reference`) — cleared

Open question 2 now reads:

> That clause sits in the §3 sentence ending `and the §3 status line above
> carries that pinning.`; Pair 3's OLD is in the sentence after it, and neither
> pair edits the clause.

Master, measured at source/gdd.md line 1533:

> each commit cited since is pinned at the landing that cites it, and the §3
> status line above carries that pinning. That form was ruled on 2026-08-05, and
> the ruling is confined to this sentence: it matches the §3 status line above,
> whose substance is unchanged

The clause sits in the sentence ending "carries that pinning."; Pair 3's OLD
sits in the next sentence, which begins "That form was ruled on 2026-08-05".
The attribution is now correct, and line 1533 is in §3 (headings at 1425 and
1544, measured as above). No pair's `**OLD**` covers the clause.

### The third change — Pair 2's `Note`, edited but not filed

Reported by the author rather than made silently. Checked independently, claim
by claim, against `source/gdd.md`:

- "there is no longer a crew commit *the document stands at*" — Pair 1's `**NEW**`
  removes the phrase `This draft stands at`, whose sole occurrence is at line
  1516 (1 hit document-wide, occurrence-level).
- "The manifest the sentence turns on is the one that records `dataCommit`,
  which the master places in the UE tree" — the same §3 text at line 1516 that
  Violation 1's repair cites. This is the site of the same mis-grounding, and it
  is now grounded on `Data/StratData.manifest.json`, not on
  `StratRules.manifest.json`.
- "the passage's own two examples read it at UE project commits" — measured at
  source/gdd.md lines 2707–2711: "The manifest recorded [`862a225`](…) at
  `0897cb5` and records [`c2f5860`](…) at `4ceaf93`". Both `0897cb5` and
  `4ceaf93` are in F3's UE-half table; neither appears in F3's crew-half table.
  Two examples, both at UE project commits.
- "The rule the sentence states is untouched" — the ruled rule immediately above
  Pair 2's OLD (source/gdd.md lines 2703–2705, "**The manifest's `dataCommit`
  names the commit the vendored bytes came from, and it advances when and only
  when those bytes change (ruled 2026-08-06).**") is not covered by any pair's
  `**OLD**`.

So the third change repaired the same defect at a second site, and its repair is
correct. **One limit on that finding, stated as a limit:** I verified the Note as
it now stands; I did not recover the pre-edit text, so the author's account that
the old Note carried the identical wording is not something this pass measured.
The current text is true and grounded regardless of what it replaced.

### Re-checked because the edits could have disturbed it

- Addendum shape is complete: `Placement`, `Draft` (three `### Pair n` blocks of
  `**OLD**`/`**NEW**`), `Change requests`, `Open questions for the Director`,
  `Grounding`. `Disposition of every candidate` and `Handoffs` are banned from
  this shape; their absence is not a finding.
- All three `**OLD**` strings re-measured at occurrence level (not line level):
  `This draft stands at` 1 hit (line 1516), `document stands at` 1 hit (line
  2707), `whose substance is unchanged` 1 hit (line 1533). Uniqueness holds.
- Placement holds: Pair 1 and Pair 3 under `## 3. AI Architecture — how AI agents
  are used (roles)` (line 1425); Pair 2 under `## 4. Technical Strategy`
  (line 1544).
- No pair edits the §3 clause F5 names, and F6's reasoning does not appear in any
  `**NEW**`.
- The pairs touch §3 and §4 only, so `kb_rules.md` — a parse of §2 — is not made
  wrong by them. No `kb-desync`.

Not re-done, per the first pass and unmoved by these edits: F3's eleven late
shas and their occurrence counts, the absence of any ceiling dependence, and
Pair 3's `that ruling` (which stands in for the 2026-08-05 reachability ruling
named in its own sentence, not for the `T-INT-02` / `T-INT-03` / `T-SAVE-06`
no-closure finding).

---

## `source/FACTS_stamp-scope.md` — PASS (0 violations)

Both corrections were re-measured rather than taken on trust.

**F2 / Subject — the stamp's position.** `^.{218}This draft stands at` returns
1 hit at source/gdd.md line 1516, so exactly 218 characters precede the stamp on
that line, and the correction's offset of 218 is right on the zero-based reading
it uses. The preamble those 218 characters hold is
`*Status: live tracker — first rows populated 2026-07-26 … (wk 1–3, §4.4). `,
so the correction's claim that the preamble ends "(wk 1–3, §4.4)." also holds.
The correction's collateral re-measurements hold too: `^.{101086}$` returns
exactly 1 hit in the file, and line 1515 is blank.

**F2 — the count of 8.** Enumerated at occurrence level, document-wide:
`end of this paragraph` returns 8 hits, all on line 1516; `recorded at the end of
this paragraph` returns 6 of those 8. The remaining two read
`an eighth**, counted at the end of this paragraph` and
`as since been ruled, at the end of this paragraph`, exactly as the correction
states. The count of 8 belongs to `end of this paragraph`.

**Marking in place.** Both corrections are blockquoted beside the claims they
correct rather than edited over them, and each states what it supersedes and
what survives. The superseded wording therefore still appears above each
correction; that is the convention this kit requires, not a contradiction, and
the re-reading each correction supplies is unambiguous. The pre-send declaration
is likewise marked false in place with what it certified and did not left
visible. Nothing in the block is left asserting both sides of a corrected claim.

---

## Verdict

**PASS.** `sections/tech_stamp-scope.md` carries zero violations: the Grounding
now grounds Pair 2's manifest on `Data/StratData.manifest.json`, the file §3
line 1516 places in the UE tree and §4 lines 2683–2684 name, and Open question 2
now attributes its clause to the sentence ending "carries that pinning" at line
1533 rather than to the sentence Pair 3 edits. The one unfiled change — Pair 2's
`Note` — was the same mis-grounding at a second site and its repair is correct,
with the caveat recorded above that this pass verified the new text and not the
old. `source/FACTS_stamp-scope.md` carries zero violations: both in-place
corrections re-measure true and leave the block self-consistent. Nothing further
is required before merge; the Director may apply the three pairs at the
placements the draft specifies, and should then rebuild the derived files and
re-sync, since §3 and §4 both move.
