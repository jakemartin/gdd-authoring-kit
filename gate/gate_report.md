# Gate report — run `editor-pass-4`

Master: `source/gdd.md` @ md5 `e1d369273c274649f2e72f9f51806cba`
(`source/MANIFEST.txt` present; the run reads current material).

Sections gated: 1. Top-level verdict: **PASS**.

| File | Verdict | Violations |
|---|---|---|
| `sections/tech_editor-pass-denotation.md` | PASS | 0 |

---

## `sections/tech_editor-pass-denotation.md`

No violations.

Every probe below was run on this file's own bytes rather than inherited from
`editor-pass-3`. Patterns were written to tolerate inline emphasis and a wrap at
any interior word boundary (`\s+` between words, `-\s*` for the hyphen,
multiline mode), because a literal-space probe fails silently on this master —
that failure mode is what produced the corrected `in-editor Automation harness`
figure, and it caught me once in this run too (see *Pair 8's quotation* below).

### The two `editor-pass-3` findings, re-checked

- **The census universal is gone, not narrowed.** `every occurrence counted`
  returns zero in the draft. What stands in its place is
  `**Among** what that reading found are occurrences naming the runner under …`
  followed by `That is not a claim about every occurrence of those strings, and
  one of them is a pair site: line 1585's …`. That is an existential with its
  witness exhibited, and the witness is the very site my previous finding named.
  It is not falsifiable by line 1585 the way its predecessor was. Read
  exhaustively — "exactly one occurrence fails" — it would be false, since the
  1514 (×2) and 3105 occurrences inside `Whether *the editor pass* is meant to
  carry those subjects` are pair sites too; but the immediately preceding clause
  disclaims exhaustiveness in terms, so the exhaustive reading contradicts the
  sentence it sits in. Existential, and clean.
- **Pair 6's note no longer claims four IDs had none.** `four that had none`
  returns zero. The replacement is
  `` `T-SAVE-06`'s tally-shaped outcome becomes a stated one, and `T-INT-02`,
  `T-INT-03` and `T-INT-05`, which the cell scheduled without giving any outcome
  of their own, now have one ``. This was the closest call in the run, and I
  weighed filing it: the master's sentence at line 1567 —
  `**One still waits**: `T-SAVE-06`, on the in-editor Automation harness it is
  asserted jointly with `T-INT-02` on.` — *does* state a disposition for
  T-SAVE-06, and `becomes a stated one` could be read as denying that. It does
  not survive as a violation, for two reasons on the bytes: the note grants
  T-SAVE-06 an outcome in its own words (`T-SAVE-06`'s … *outcome*) and
  contrasts it with three that had `no outcome of their own`, which is exactly
  the distinction the previous finding demanded; and `tally-shaped` is true of
  the master's form, whose main clause is the cardinal `One still waits`. The
  claim is about the form of an outcome that exists, not about its absence.
  Cleared, with the reasoning shown because a reader could reach the other one.

### The nine pairs — probed fresh, since a stale clearance was the one way a pair could still be wrong

I treated the pairs as unverified rather than assuming four runs of clearance.
Each OLD was re-probed as a literal regex over the current master, with `-o` so
occurrences on one physical line could not hide inside a line count:

- Pair 1 — line 2859, whole line, `^…$`. One occurrence.
- Pair 2 — line 1514, one occurrence, distinguished by its trailing
  `**`T-SAVE-07` did not close:**`.
- Pair 3 — line 1514, one occurrence, trailing
  `` `cpp_reference/selfplay.cpp` is untouched. ``. Pairs 2 and 3 sit in two
  different row-10 records — part (b)'s and part (c)'s — on one physical line;
  their spans are disjoint, so the note's "the other §3 record" holds and there
  is no placement collision.
- Pair 4 — line 3105, one occurrence, §4.11.
- Pair 5 — line 1585, one occurrence, §4.5.
- Pair 6 — line 1567, one occurrence.
- Pair 7 — line 1633, whole line, `^…$`. One occurrence. Line 1634 begins
  `does not`, as the note says.
- Pair 8 — lines 2790–2793 in multiline mode with both internal breaks and the
  period inside the quotation marks. One occurrence.
- Pair 9 — line 1567, one occurrence, disjoint from Pair 6's span.

Section boundaries confirmed against the heading index: §3 = 1423–1541 (1514,
1531), §4.4 = 1561–1574 (1567), §4.5 = 1575–1586 (1585), §4.7 = 1625–2651 (1629,
1633), §4.9 = 2729–2923 (2790, 2859), §4.11 = 3041+ (3105). Every placement the
draft states matches the section its anchor is in.

Pair 1's insertion checked in place: line 2860 reads `editor-pass IDs need
besides it are the subjects named here`, so "besides it" still resolves to the
harness after "It is also not sufficient" becomes "The harness is also not
sufficient"; and lines 2853–2854 read `It waits on **an in-editor Automation
harness**`, which is the name Pair 1's NEW points at rather than a new one.

### The framing prose — the test the last four findings all failed

Applied to every sentence in the notes, Checks and change requests: *is this
asserting something about `source/gdd.md` that has not been measured here?*

- **The census's seven string figures all reproduce**, measured occurrence-wise
  under the draft's own patterns: `editor\s+pass` = 25 (9 on 1514, 1529,
  1531 ×2, 1585 ×2, wrapped 2529–2530, 2726, wrapped 2810–2811, 2921, 3038,
  3058, wrapped 3084–3085, 3105, 3139, 3142, 3147); `in-\s*editor\s+pass` = 8,
  so bare = 17; `editor-\s*pass` = 1 (2860); `in-\s*editor\s+Automation\s+
  harness` = 14; `in-\s*editor\s+Automation\s+pass` = 3 (1585, 1644, 3063);
  `in-\s*editor\s+Unreal\s+Automation\s+parity\s+pass` = 1 (1514); and
  `in-\s*editor\s+Unreal\s+Automation\s+pass` = 0.
- **The AA sweep is exhaustive on the bytes.** I read all 26 occurrences in
  their own sentences, including the four the draft's own windows would not
  have shown on a single-line probe (1529, 3142, and the wrapped 2529–2530 and
  3084–3085). Every occurrence outside the pairs either schedules an ID *into*
  the pass (2726, 2921, 3037–3038, 3139, 3142, 3147), says no pass exists at a
  commit (1514 ×4, 1529, 1531 ×2, 1585, 3058), or says the pass is not yet due
  (1514, 3084–3085) — all consistent with the denotation, none defining or
  reserving. Exactly three reserve the question (1514 ×2, 3105) and are Pairs
  2–4; exactly one equates IDs with the runner (1585) and is Pair 5. Pair 4's
  kept cardinal, "The remaining site that reserves the question", is earned by
  that sweep.
- **The AB sweep is exhaustive.** §4.4 has seven milestone cells. Week 2 states
  `T-INT-01/04 and T-SAVE-04 close here, the rest do not`; weeks 1, 6 and 7
  schedule no acceptance ID; weeks 4 and 5 state the disposition of what they
  name. Week 3 is the only cell that schedules IDs to close and leaves some
  without one. Pair 6's note's account of what week 3 schedules and reports
  green matches line 1567 word for word.
- **The AC sweep reproduces.** `pure\s+C\+\+1?7|C\+\+\s*17|C\+\+\s*20|std:c\+\+|
  std=c\+\+` returns exactly two hits, 1629 and 2790, so "the document states no
  other language-standard value" is measured, not assumed.
- **The sufficiency sweep reproduces at four hits** — 1006 (§2.13.1,
  `measurement is the only thing that catches it being wrong`), 1514 (§3, which
  already reads `among what it still waits on are the in-editor Automation
  harness and a vendored replayer`), 1567 (Pair 6), 3105 (§4.11 row 10,
  `**`T-SAVE-06` is now the only ID this row lacks**`, true over that row's own
  T-SAVE-01..07 set). Each disposition the draft gives them is correct.
- **The new "Note sweep" Checks bullet is accurate.** I re-ran its test myself
  over all nine `*Note.*` blocks. Every surviving cardinal, ordinal and "both"
  is either about this file (Pairs 2–4, Pairs 7 and 8, "the two cannot both
  stand") or measured against the master and reproduced above ("the whole of
  source line 2859", "spans source lines 2790–2793", the week-3 schedule
  enumeration, "the other §3 record", "The remaining site"). I found no
  surviving cardinal asserting something about the master that this file has
  not measured, which is what the bullet claims. Its clause "those kept are
  recorded in the report for this round with their grounding" points at the
  author's round report rather than at a file in `source/` or `sections/`; it is
  not a citation of a GDD section, unit, file, commit or test ID, and the kept
  cardinals do carry their grounds inline at the pairs, so it is not filed.
- **Pair 8's quotation.** `an MSVC compile through UBT, under the engine's own
  flags` returned zero on a literal probe — my own silent failure this run. The
  text is on the master at 2811–2812 as `an MSVC` / `compile **through UBT,
  under the engine's own flags**`: a wrap plus inline bold. The quotation is
  accurate; my first probe was not. Recorded so the zero is not read as a
  finding by anyone re-running it.
- **Pair 9's "Only the verb moves"** was examined and not filed. The pair also
  inserts a comma after "complete set" and rebuilds the predicate into a clause
  with a new subject ("this week"), so read at maximum strictness the phrase
  understates the edit. It is bounded in the same sentence by an enumeration
  that is exactly true — the ID list, the row attributions and the T-AI-06
  composition are byte-identical between OLD and NEW — the merge is driven by
  the pair's bytes rather than by the note, and no statement in `source/gdd.md`
  is contradicted by it. Not a violation; noted because it is the one remaining
  sentence in the file whose wording is looser than what it describes.

### The four constraints named for this run

- **Ruling AA is stated once.** Pair 1 states the denotation in §4.9. Pairs 2, 3
  and 4 replace their reserving clauses with `Both what *the editor pass*
  denotes and what running it does not supply are stated at §4.9` — a citation
  carrying no definition. Pair 5 cites `(§4.9)` and defines nothing. Pair 6
  cites `(§4.9)` four times and defines nothing. Pairs 7 and 8 name §4.9 as the
  divergence tracker, not as a denotation.
- **No replacement cardinal for the §4.4 tally.** Pair 6's NEW contains no
  cardinal at all; each of the four dispositions reads "among what it waits on",
  so no sufficiency claim is made and none goes false when a further blocker is
  found. Each disposition is grounded on the master: T-SAVE-06 and T-INT-02 on
  the harness, the vendored replayer and the `Replay` vendoring ruling (2861–2866);
  T-INT-03 on the unbuilt command surface (2862–2863); T-INT-05 on real
  Stratocracy widgets `measured absent at a13626f` (2863–2867); and row 9's
  non-closure at 3080–3082.
- **No conformance-mode claim.** Pairs 7 and 8 state `-std=c++17`, `/std:c++17`
  and `/std:c++20` and nothing else about compiler settings; neither asserts the
  named configurations are the complete set, and the "pure C++17" claim at 1629
  is outside both OLDs and stays.
- **The pinned figures are unmoved.** §4.5's 71 / 61 / 10 and the 9 verified
  ledger rows are untouched by every pair, Pair 5 included — it edits inside
  line 1585 without touching a cardinal, and the `**3** left in row 9` sits
  outside its OLD. No acceptance ID is minted, closed or re-opened; no ledger row
  is created, flipped or removed; no register row is minted.

### Also checked

- **Placement.** One file, nine pairs, nine disjoint byte spans; two pairs share
  line 1514 and two share line 1567 without overlapping. No collision, and every
  placement is mechanically mergeable from its OLD.
- **kb desync.** No pair touches GDD §2 (all nine land in §3, §4.4, §4.5, §4.7,
  §4.9 and §4.11), so `kb_rules.md` is unaffected and no `kb-desync` is owed.
- **Change requests.** Both are proposals to the Director rather than prose
  changes: CR1 declines to standardise the runner's several names and points at
  Checks for the spellings and the reading; CR2 flags that Pairs 2 and 3 edit
  sealed §3 records. Neither states a number, and neither is a violation.
- **Format.** The file uses the OLD/NEW addendum form this project has merged
  and sealed across previous rounds, with placement carried per pair and
  Grounding present. No `format-breach` filed.
- **The short md5.** The draft writes `e1d36927`; `source/MANIFEST.txt` carries
  `e1d369273c274649f2e72f9f51806cba`. A prefix of the pinned value, not a
  competing figure.

---

## Verdict

**PASS.** The nine pairs are byte-exact, uniquely anchored and unmoved, and I
re-probed every one of them rather than inheriting the earlier clearances, since
a stale clearance was the only remaining way a pair could be wrong — none was.
Both `editor-pass-3` findings are repaired at the root rather than patched: the
census's universal is deleted and replaced by an existential that exhibits the
very occurrence that falsified it, and Pair 6's note now distinguishes
T-SAVE-06's tally-framed outcome from the three IDs the cell left without one.
The four cardinals the author found unprompted and the three it rewrote in the
final sweep all survive the test that produced every earlier finding — each is
either about this file or measured against the master, and I reproduced each
measurement independently, including the full 26-occurrence AA sweep, the seven
census figures, the AB, AC and sufficiency sweeps and the pinned §4.5 figures.
Nothing must happen before merge: `sections/tech_editor-pass-denotation.md` is
accepted at run `editor-pass-4`, and the Director may merge it at the placements
each pair states, honouring change request 2's flag that Pairs 2 and 3 edit
sealed §3 records, then rebuild the derived files and re-run `python sync.py`.
`kb_rules.md` needs no re-sync from these pairs, since none of them touches §2.
