# Gate report — run `row5-links-2`

- **Master**: `source/gdd.md`, md5 `5bad314bcb34e52a88bff92727f5fcc5` (from `source/MANIFEST.txt`).
- **Sync**: `source/MANIFEST.txt` present. Three entries — `gdd.md`, `kb_rules.md`, `kb_setting.md`.
- **Top-level verdict**: **PASS**
- **Total violations**: **0**

---

## `sections/tech_row5-links.md` — **PASS**, 0 violations

No violations filed.

### The `row5-links-1` violation is cleared

The blocking sentence — *"Everything else is bare for every commit: … the §4.5 risk cell's
green-count list, and §4.11's build-order prose"* — is absent from the file. It is not restated
in narrower form anywhere: `rg` over the draft for `bare for every commit`, `Everything else`
and `every commit` returns no surviving instance of the claim. The correct version of the fact
survives where it was already correct, in `## Sites deliberately left alone`
(*"In that cell `c224825`, `647d4df`, `ad77b13` and `d8284f1` are all bare and only `9086d6a`
is linked; the majority form is bare"*) and in Open question 1. That matches §4.5 line 1582 as
merged, which links `9086d6a` and leaves `c224825`, `647d4df`, `ad77b13`, `d8284f1` and both
mentions of `6ccd40b` bare. Nothing in this round's edit reintroduces the falsified universal.

### The deletion did not leave a hole

This was the one thing worth re-deriving, and it was checked as three separate failure modes.

**Stranded connective.** The surviving derivation runs: three enumerated structural positions →
*"That yields four link sites for `6ccd40b` — …"* → *"After the patch `6ccd40b` reads 4 linked /
10 bare"*. Each sentence's antecedents are present. The fourth site (the *Status*-line head-commit
clause) is not one of the three enumerated positions, and the sentence supplies its own
justification inline — *"whose immediate neighbour `9086d6a` is already linked in the same clause
as its parent"* — verified at line 1511, where the parent citation reads
`whose parent is [`9086d6a`](…)`. No dangling *"these three"*, no orphaned demonstrative.

**Orphaned back-reference.** `## Sites deliberately left alone` ends its third bullet with
*"as set out above"*. Its two nearest conjuncts are set out above: pair 3's note
(*"The cell's second mention of `6ccd40b` … stays bare"*) and pair 4's note
(*"The later "closes at one commit — `6ccd40b`, not `ad77b13` —" stays bare"*). The bullet's
own text names the third item explicitly rather than relying on the back-reference. Nothing is
referred to that no longer exists.

**Argument now asserting more than it supports.** The lead sentence *"`6ccd40b` is given a link
at the sites its sibling commits carry one, and left bare at the sites they are bare"* is
qualified by the sentence immediately after it — *"three structural positions carry a link
**every time**"* — so the operative scope is positions where the sibling form is unanimous.
§4.5 is not such a position, and the draft does not silently absorb it: it is named in
`## Sites deliberately left alone`, given a stated reason, and filed as Open question 1. That is
disclosure, not an overclaim, and it is the distinction the `row5-links-1` violation turned on.
The deletion went exactly as far as the claim's falsity did, and no further.

### Re-checked independently, not taken on report

- **Five anchors, five replacements, no insertion.** Every `OLD` matches **exactly once**
  document-wide by occurrence counting: pairs 1 and 2 at line 1511, pair 3 at 1520, pairs 4 and 5
  at 1528. No `NEW` contains its `OLD` as a verbatim prefix, so all five are replacements, as the
  Placement header declares. Markers sit on their own line before each fence; pair headings are
  at `##`.
- **The 16-mention census.** `rg -o` returns exactly sixteen occurrences of `6ccd40b`: eight at
  1511, two at 1520, three at 1528, two at 1582, one at 2744 — byte-for-byte the Grounding
  section's figures.
- **The 4 / 10 / 2 arithmetic.** Pairs 1–2 leave five bare mentions at 1511; pair 3 leaves one at
  1520; pairs 4–5 leave one at 1528; 1582 keeps two; 2744 keeps one. Ten bare, four linked, two
  deleted, summing to sixteen — and matching `## Sites deliberately left alone` item for item.
- **The chosen link positions.** The landing announcement is linked for `647d4df`, `ad77b13`,
  `d8284f1` and `9086d6a` at 1511; every evidence cell at 1515–1525 links its commit except row
  5's; the *"joined at"* sentence below the table is linked for `c224825`, `647d4df`, `ad77b13`,
  `d8284f1` and `9086d6a` at 1528. No exception found.
- **Sibling shape unchanged by the patch.** No `NEW` alters a sibling's link form, so
  `647d4df` (3/6), `ad77b13` (3/7) and `d8284f1` (3/6) stand as stated, and after the patch no
  commit is linked at every mention.
- **Scope item 4's negative.** Case-insensitive search for `pushed` / `unpushed` / `GitHub` /
  `working repository` / `carries no link` / `without a link` / `reachable in the working` over
  the whole file returns hits at only two sites — `without a link` at 1511 and
  `carries no link` / `not yet pushed` / `reachable in the working` / `GitHub` at 1528 — both
  inside pair 1's and pair 5's `OLD` respectively. Line 1511's `not citable` is about the
  untracked `build/` binary, not `6ccd40b`. No third site survives the patch asserting that
  `6ccd40b` is unpushed or unlinkable.
- **Open question 1's link claim.** The only commit links outside §3 are at 1582 (§4.5) and 2504
  (§2.13, Q32), exactly as stated.
- **§4.11's bare passage.** Lines 2742–2745 cite `5ffa8d6`, `c224825`, `647d4df`, `6ccd40b`,
  `ad77b13` and `d8284f1`, all bare — the bullet's claim holds.
- **`links` → `cites` reversion.** Post-patch §3 cites `5ffa8d6`, `c224825`, `9f87ecd`,
  `647d4df`, `ad77b13`, `d8284f1`, `9086d6a` and `6ccd40b`; the head of `main` is `6ccd40b`
  itself, so the wider claim is true of the patched document and the narrowing has no remaining
  work to do.
- **Grounding vs. draft, claim by claim.** Every substantive figure in the draft traces to a
  Grounding bullet and to a line in `source/gdd.md`. The one externally supplied fact — that
  `https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b` resolves unauthenticated — is
  labelled as supplied rather than inferred, which is the correct disclosure.
- **Format.** Placement, Draft, Change requests, Open questions and Grounding all present. Change
  requests correctly empty: no number, rule or evidence claim moves. Build order correctly
  records no row movement. No `kb_rules.md` exposure — this round touches §3 only, and the KB is
  parsed from §2.

---

## Verdict

`sections/tech_row5-links.md` **PASSES** with zero violations, and the top-level verdict for run
`row5-links-2` is **PASS**. The `row5-links-1` `contradiction` is cleared by deletion rather than
by restatement, and the deletion left no stranded connective, no orphaned back-reference and no
surviving claim that outruns its support — the remaining derivation asserts only the positive
link positions, each of which I re-measured on the merged master. Nothing must happen before
merge beyond the ordinary sequence: apply the five pairs byte-for-byte at their verified anchors
in the order given, confirm after application that `6ccd40b` reads four linked and ten bare and
that no *"not yet pushed"* or *"carries no link"* text remains anywhere in the file, then rebuild
the `.pdf` and `.txt`, and re-run `python sync.py`. The two open questions — §4.5's mixed link
form and the *"— `d8284f1`, row 6's, included —"* aside — are the Director's to rule and are not
conditions on this merge.
