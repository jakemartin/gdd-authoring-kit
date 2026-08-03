# Gate report — run `cleanup-3`

- `source/MANIFEST.txt`: present (no `sync-missing`).
- `gdd.md` md5 at this run: `324dfa07c91fc4ddec4c5315ba1c397b` — unchanged from `cleanup-1` and `cleanup-2`. `kb_rules.md` and `kb_setting.md` read.
- Files in scope: `sections/tech_cleanup-and-t-cap-05.md` (one file).
- Out of scope, sealed and already inside this snapshot: `sections/rules_t-cap-alias.md`, `sections/tech_row6-opponent-ai.md`.

**Top-level verdict: PASS.**

---

## `sections/tech_cleanup-and-t-cap-05.md` — PASS

**Violations: 0.**

The `cleanup-2` violation is discharged. The false sentence `All six are replacements,
none an insertion.` returns **zero** matches in the file. Its replacement carries all four
elements the fix required — the five/one split, pair 3 named as the insertion, the
post-check expectation stated as OLD count **1** for pair 3 and **0** for the other five,
and the not-safe-to-apply-twice consequence:

> **Five of the six pairs are replacements; pair 3 is an insertion** — its NEW block opens
> with its OLD anchor verbatim and appends one sentence after it … The insertion-aware
> post-check should therefore expect pair 3's OLD to return **one** match after
> application, and the other five to return **none**. … **this file is not safe to apply
> twice**: a second application would append pair 3's sentence a second time.

### What I re-derived this run rather than accepted

**Anchor uniqueness — all six, independently.** Each OLD block was matched against
`source/gdd.md` as a literal, pairs 2 and 5 multiline with their internal line breaks and
leading indentation as written. Each returns exactly **one** match:

| Pair | GDD site | Matches |
|---|---|---|
| 1 | §4.11 table, row 9 *Depends on* (line 2694) | 1 |
| 2 | §4.7 register preamble (lines 2383–2385) | 1 |
| 3 | §4.7 register, Q6 *Assumption* cell (line 2404) | 1 |
| 4 | §4.7 register, Q14 *Blocks* cell (line 2412) | 1 |
| 5 | §4.7 Stub 8 fenced block (lines 2328–2332) | 1 |
| 6 | §4.11 table, row 8 *Acceptance test IDs* (line 2693) | 1 |

**Replacement vs. insertion — derived per pair, not taken on report.** A pair is an
insertion only if its whole OLD block is a substring of its NEW block. Pair 3 is; the other
five are not, and each fails for its own reason, which I checked individually rather than
in aggregate:

- pair 1 rewrites the clause outright;
- pair 2's third line goes `tally suite) now assert.` → `tally suite less T-CAP-05) now assert.`, so the three-line block does not survive;
- pair 4 deletes `and no gate of its own`;
- pair 5's block is split — the inserted `GATE-CAP-PARTIAL` lines land between the OLD block's first line and `Determinism:`, and the OLD's final `T-UI-03..04 in-editor Automation.` gains `; GATE-CAP-PARTIAL headless…`, so neither the block nor its last line survives;
- pair 6's `†**) |` becomes `†**) + GATE-CAP-PARTIAL |`.

This is a fourth independent derivation and it agrees with the file. The Grounding's
post-check instruction is correct as written.

**Byte-level spot-checks, since a re-emitted block is where a character quietly changes.**

- U+2212 preserved: `69 − 42 = 27` at line 148 matches a U+2212 search.
- `†` present at all seven expected sites (lines 81, 83, 90, 94, 111, 142, 162); pair 6's OLD matched anchored to line start **and** line end, so the `**T-UI-03, 04 †**` run is byte-identical.
- No curly quotes anywhere in the file — pair 5's `"objectives held"` uses the same straight quotes as §2.8 line 367.
- No U+00A0 anywhere in the file. En dashes in `rows 4–5` and `Spec Stubs 1–7` match the GDD's.
- Pair 5's OLD matched with its literal 11-space and 9-space indents, so the carried Determinism span is byte-identical including leading whitespace.

**Grounding checked claim by claim against `source/`.**

- 69 / 42 / 27 / 26-in-rows-7–10 — §4.5 line 1558, verbatim.
- "no new ID has been written since `c224825`" — §4.5, verbatim.
- "row 6's GATE-AI-SMOKE is acceptance that deliberately mints none" — §4.5, verbatim.
- "minting a `T-` ID here would move §4.5's count" — verified in `E:\MultiAgent\stratocracy-crew\spec\ai_spec.md` line 68, verbatim. This is a quotation of a file outside `source/`; it is accurate.
- §4.11 row 6's acceptance cell carries the check with no `T-` ID (`T-AI-01..06 + self-play smoke`) — line 2691. The draft's Open question 3 already records that this cell names it descriptively while pair 6 names it by its `GATE-` name; that is filed, not asserted away.
- Both snapshot fields exist: `captureProgress` per-unit (line 2311) and `objectivesHeld X of N` per-side (line 2312). The check adds no field.
- "A marked ID may not guard a rules invariant" — §4.11's † paragraph (line 2699) and its T-INT-03 bullet (line 2734). §4.7's cut-line paragraph (line 1620) does state the narrower critical-path version, as the Grounding says.
- Row 8 holds no code — §3 ledger, `| UI | *pending* | — | *pending build* |` (line 1502).
- T-CAP-05 aliases to nothing — §2.8 alias map line 383, and line 388's exception paragraph.

**Handoff anchors verified greppable.** `no gate asserts it end to end, and it appears in
no acceptance set.` is at §2.8 line 391. `| T-CAP-05 | **nothing** | see below |` is at
line 383, character for character. `GATE-CAP-PARTIAL` returns **zero** matches against
`source/gdd.md` at this md5, as the file claims.

**Placement.** Every cell name checks out against its own table header: §4.7's register
header is `| ID | Question | Blocks | Assumption in force until ruled |` (line 2397), and
§4.11's is `| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |`
(line 2684). The six sites are pairwise disjoint — 2328–2332, 2383–2385, 2404, 2412, 2693,
2694 — so the stated order-independence holds. Nothing lands in §4.11's preamble or its †
bullets, in Spec Stubs 1–7, or in §1, §2, §3, §4.4, §4.5, §4.8, §4.9 or §4.10, as claimed.
One file in this run, so no cross-section collision is possible; pair 4's anchor already
carries the alias ruling's `and no gate of its own` text, which confirms it is written
against the post-merge snapshot and not a stale one.

**No stat-drift.** The only numbers in the file are 69 / 42 / 27, which match §4.5, and
70 / 28, which appear solely inside Open question 1 as the priced cost of an alternative
the Director has not taken. `Change requests: None` is correct — no pair moves a number.

**No kb-desync.** `kb_rules.md` is a parse of §2; no pair touches §2, and `kb_rules.md`
contains no `T-CAP` string at all, so nothing there is falsified. The §2.8 sites that
*will* go stale are named, quoted and handed to `rules-designer` rather than edited.

**No unverified-claim.** Every site that names `GATE-CAP-PARTIAL` states it as written,
unblocked and asserting, and explicitly **not run and not green** — pair 2 ("row 8 holds
no code, so that gate has not run — it asserts, and it is not green"), pair 4 ("so that
gate has not run and T-CAP-05 is not green"), and the handoff's residual-fact sentence.
No commit or test ID is claimed for it anywhere.

### Considered and not charged — recorded so it is not re-litigated

- **Pair 5 says "raising a unit's captureProgress", while Q4 rules that progress is held by the tile.** Stub 8's own snapshot field list puts `captureProgress` in the per-unit record (line 2311), so the check restates the GDD's existing field placement rather than contradicting Q4; the tension is pre-existing in `source/`, and Open question 4 names it and states the check does not depend on the answer. Not a violation.
- **The Placement row for pair 2 names the "No row now states *no reading*" sentence, while the anchor sits in the sentence after it,** inside the same bolded passage. The OLD block is exact and unique, so the merge is still mechanical. Loose, not wrong.
- **No heading literally named "Draft".** The six OLD/NEW pair blocks are the draft, in the addendum shape this project has merged repeatedly and that `cleanup-1` and `cleanup-2` both accepted. Not filed.
- **The Handoffs bullet's "§4.11 row 8's acceptance cell"** — carried forward from `cleanup-2` as loose rather than false, unchanged this round, and left alone as instructed.

---

## Verdict

`sections/tech_cleanup-and-t-cap-05.md` passes with zero violations, and run `cleanup-3`
is therefore **PASS**. The single `cleanup-2` violation is fixed exactly and only — the
false sentence is gone, its replacement states the five/one split, the asymmetric
post-check and the do-not-apply-twice consequence, and nothing else in the file moved that
I can detect at byte level. The file is clean and may be merged as written: apply the six
pairs in any order, then run the post-check expecting pair 3's OLD at **one** match and
the other five at **zero**, and apply the file exactly once. The §2.8 work the merge
creates — the "no gate asserts it end to end, and it appears in no acceptance set."
sentence and the `| T-CAP-05 | **nothing** | see below |` alias row — is a handoff owed to
`rules-designer` after these pairs land, not a defect in this draft.
