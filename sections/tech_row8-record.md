# Technical design — row8-record addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All thirteen pairs were merged into the master GDD on 2026-08-04.
> Master md5 `83899833551abbe9d4518e21fd771520` →
> `d2cfe86d6decad525a9a002d3f2c17b8`.
>
> **Twelve pairs are replacements. Pair 4 is an INSERTION** — its NEW opens with
> its OLD verbatim — so **that one anchor survives on the merged master by
> design** and the file is not safe to apply twice. The classification was
> re-derived from the current bytes after the remediation round, not carried over
> from the first draft: Pair 3's span was extended there, and it remains a
> replacement. Every OLD was verified against the **master** before anything was
> written, each matching exactly once, and the apply refused to write unless all
> thirteen did.
>
> Gate: run `row8-record-2`, **PASS**, 0 violations, after `row8-record-1`
> (BLOCK, 4). The one that mattered was a `contradiction`: Pair 3 widened §3's
> claim that *"everything on that path but row 8 is now evidence rather than
> schedule"* to cover the whole critical path, while leaving standing — and
> declaring unchanged — the clause *"since `T-TURN-10`, the one path ID that was
> written and asserting without being green"*. That clause was true only because
> of the exclusion the widening removed, and row 8's own `T-UI-03` and `T-UI-04`
> are in exactly that state, so two path IDs answer it. Fixed by extending Pair
> 3's span and restating the clause. The other three: the driver's `snapshot`
> command was ungrounded (grounded, not deleted — the command is real and
> `GATE-DRV-12` asserts it; the first gate run had been given a driver fact set
> that omitted it, which was **the orchestrator's error, not the author's**), and
> two Grounding sweep counts were wrong — `critical path` is seventeen lines, not
> fourteen, and `GATE-CAP-PARTIAL` eight, not five.
>
> **What this round did:** recorded §4.11 row 8's landing at
> [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303),
> parent `6ccd40b`. **The row does not flip** — `T-UI-03` and `T-UI-04` are
> in-editor Automation with no editor pass at this commit, so Q29 leaves a
> partial pass and `*pending*`, the posture row 2 holds on T-DATA-05. §4.5 goes
> **50 → 52 green** and **20 → 18 unclosed**; written stays **70** and the
> verified-ledger-row count stays **9**.
>
> **§2 DID change this round** — Pair 1 edits §2.8's T-CAP-05 exception block, 8,258
> → 8,414 chars. **`kb/rules.md` still needed no re-sync**, and that was decided by
> reading the KB rather than by the identifier: `T-CAP-05` and `GATE-CAP-PARTIAL`
> occur zero times in it, and its own line — *"a capture in progress counts for
> nobody until the objective flips"* — states the **invariant**, while Pair 1
> changes only the gate's **run state**, which the KB does not carry.
>
> **One whitespace-only change was made after the gate PASS and is recorded
> here:** the merged Pair 1 left a 120-character line in a paragraph hard-wrapped
> at ~70, so it was reflowed. No word was altered; the over-90-character
> non-table line count returned to its pre-merge 126, and the md5 above is the
> post-reflow one.

## Placement

An addendum against the merged master (`source/gdd.md`, md5
`83899833551abbe9d4518e21fd771520`). **Thirteen OLD/NEW pairs — twelve
replacements and one insertion (Pair 4).** Pair 4's NEW block opens with its OLD
anchor verbatim and appends after it, so that anchor survives the merge by
design; the other twelve OLDs should be absent from the master afterwards. This
file is **not safe to apply twice**.

Sites: one in **§2.8** (T-CAP-05's exception block), six in **§3** (three in the
italic *Status: live tracker* line, one in the ledger table, two in the
populated-rows paragraph), three in **§4.5**'s *Specification outruns the build*
row (three disjoint spans of one cell), two in **§4.7** (the register preamble's
T-CAP-05 exception and Q14's **Blocks** cell), one in **§4.11**'s preamble.

**Pair 1 edits §2.** The merge checklist's `kb/rules.md` re-sync therefore
applies as a question rather than automatically: `GATE-CAP-PARTIAL` and
`T-CAP-05` each occur **zero** times in `source/kb_rules.md`, so no identifier
this addendum touches is parsed into that file. §2's character count moves by
this pair alone.

No spec stub is redrafted. No acceptance ID is minted. No ledger row flips.

## Draft

---

### Pair 1 — §2.8, the T-CAP-05 exception (replacement)

The one §2 edit. No commit sha is introduced: §2 cites none today (every sha in
the document sits at line 1488 or later), so the run is referenced through §3
in §2's existing cross-reference style.

**OLD**
```
**It has not run, so
T-CAP-05 is asserting and not green.**
```
**NEW**
```
**It has since run, and §3 records the run:** it passed on a fixture
configured with `captureTurns = 2`, a state *Ferrum Crossing* cannot reach
at N = 1 (Q4). **Whether that closes T-CAP-05 is unruled** (§4.7, Q14).
```

### Pair 2 — §3 status line, the head commit (replacement)

**OLD**
```
This draft stands at 2026-08-03, at commit [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) in the crew repo, whose parent is [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a).
```
**NEW**
```
This draft stands at 2026-08-04, at commit [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) in the crew repo, whose parent is [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b).
```

### Pair 3 — §3 status line, the critical-path clause and its `T-TURN-10` tail (replacement)

The span covers the `T-TURN-10` clause that follows the exclusion. That clause
counts the path IDs written and asserting without being green, and it was true
only of the path **less row 8** — the exclusion this pair deletes. Once the
whole path is asserted, two IDs answer its description, so it is restated rather
than left standing. The `, and row 8's other dependency is **row 7**, …`
continuation after the span is outside both blocks and unchanged.

**OLD**
```
everything on that path but **row 8** is now evidence rather than schedule — **per acceptance ID as well as per row**, since `T-TURN-10`, the one path ID that was written and asserting without being green, closed at `6ccd40b`
```
**NEW**
```
every row on that path has since landed, **row 8** last and on a partial pass that leaves its ledger row unflipped — **per acceptance ID as well as per row**: `T-TURN-10` closed at `6ccd40b`, and the path IDs still written and asserting without being green are **T-UI-03** and **T-UI-04**
```

### Pair 4 — §3 status line, its tail: row 8's record (insertion)

The row-5-rebuild sentence that ends the paragraph today is bound to `6ccd40b`
and stays true there, so it is kept and row 8's record is added after it. The
anchor is taken long because *reporting a harness that did not run is the exact
failure this ledger exists to prevent* occurs **twice** in the document; the
`6ccd40b` clause disambiguates it. The paragraph's closing italic `*` is
deliberately **outside** both blocks.

**OLD**
```
**How `6ccd40b` was authored is deliberately not stated:** no harness claim is made for it, because none was established, and reporting a harness that did not run is the exact failure this ledger exists to prevent.
```
**NEW**
```
**How `6ccd40b` was authored is deliberately not stated:** no harness claim is made for it, because none was established, and reporting a harness that did not run is the exact failure this ledger exists to prevent. **Row 8 then landed**, at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303): **UI binding contract**, gated **`T-UI-01`, `T-UI-02` and `GATE-CAP-PARTIAL`, 14/14 under clang++ and MSVC both** — `g++` is still not installed on this machine — and **the 14 counts printed checks, not IDs**: those three IDs close over 14 printed lines, four of which are ungated snapshot-shape checks that carry no ID at all and are labelled as such in the run. Pass-1 `cpp_reference/Ui.buggy.cpp` is blocked at **10/14** under both compilers — **four FAIL lines over two distinct IDs**, `T-UI-02` on all three of its checks and `GATE-CAP-PARTIAL` on its differential — on two defects: the reachable highlight recomputed as a hex-distance filter rather than queried from the module, and partial credit toward `objectivesHeld` for a capture in progress, which is the reading **Q14** refuses. Five tracked sources are cited, each probed present at that commit: `spec/ui_spec.md`, `cpp_reference/Ui.h`, `cpp_reference/Ui.good.cpp`, `cpp_reference/Ui.buggy.cpp`, `cpp_reference/test_ui.cpp`. The last of those is a tenth harness, so **twelve** tracked sources define `main()` at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) — ten test harnesses, one combat duel simulator, and one debug REPL — a figure taken by enumerating them at that commit rather than by adding one to the count above. **This row does not flip.** **T-UI-03 and T-UI-04 have not run**: they are in-editor Unreal Automation over widget bindings, marked † in §4.11, and **no in-editor pass exists at this commit**. Both are printed by name with that reason before the tally and recorded in the acceptance record. Q29 requires the full acceptance set at one commit and is applied **per acceptance ID as well as per row**, so the row records a partial pass and stays unverified, which is the posture rows 2 and 7 hold. Both are **written, unblocked and asserting**; what they lack is a harness, not a rule — a different state from **T-SCN-10**, which is reserved and **unwritten** on Q26, and from **T-MOVE-07**, which cannot be written until Q2 is ruled. **No new acceptance ID was written**, so §4.5's written-ID count does not move at this landing, its green count moves 50 → 52 and its unclosed count moves 20 → 18; `GATE-CAP-PARTIAL` mints none, on the `GATE-AI-SMOKE` precedent. **`GATE-CAP-PARTIAL` ran on a fixture configured with `captureTurns = 2`.** *Ferrum Crossing* ships **N = 1** (Q4), so the shipped scenario cannot reach the state that gate asserts about at all; N is per-scenario data and the fixture sets it, so **no map was invented**, and the run states this rather than leaving it to be inferred. **Nothing was invented to fill a gap.** No buildlist query is offered, because whether `T-UI-04`'s buildlist reaches the UI as a snapshot field or as a query is stated nowhere in this document; and three known-absent snapshot fields were left absent — the per-factory record of builds taken this turn, the income rate, and §2.11.1's DONE bit. The debug driver's `snapshot` command now prints the view model rather than refusing on row 8's account, and its suite is **`GATE-DRV-01..12`, 12/12 under clang++ and MSVC both**, `GATE-DRV-12` being new at this commit; those IDs are still **not** `T-*`: the driver is not a §4.7 stub, has no row in the ledger below, and flips nothing. **How row 8 was authored differs from rows 5, 6 and 7, and is not reported in their words.** A **Claude Code session** authored it, and the same session also authored `spec/ui_spec.md`, as an elaboration of §4.7 Spec Stub 8. Each of rows 5, 6 and 7 names a Director-written stub in `spec/` that predated its build; §4.7 Stub 8 is Director-written, and the crew-repo spec derived from it is not. **Row 8 was the last unbuilt link on §4.11's critical path.** No in-editor harness is among the twelve `main()` definitions above.
```

### Pair 5 — §3 ledger table, the UI row (replacement)

Formatted on the **Content / scenario** row, the table's other partial pass, and
not on a flipped row.

**OLD**
```
| UI | *pending* | — | *pending build* |
```
**NEW**
```
| UI | agent | — | **Partial pass — not a flip.** `cpp_reference/Ui.good.cpp` + `cpp_reference/test_ui.cpp` @ [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) · T-UI-01 and T-UI-02 (2/2) headless, plus `GATE-CAP-PARTIAL`, which mints no acceptance ID and which ran on a fixture configured with `captureTurns = 2` — a state the shipped N = 1 scenario cannot reach. **T-UI-03 and T-UI-04 have not run**: both are in-editor Unreal Automation over widget bindings and no in-editor pass exists at this commit, so the acceptance set is incomplete and Q29, read per ID, keeps the row unverified |
```

### Pair 6 — §3 populated-rows paragraph, the count (replacement)

**OLD**
```
**Nine rows carry a ✓ in the table above, and two more carry evidence without one.**
```
**NEW**
```
**Nine rows carry a ✓ in the table above, and three more carry evidence without one.**
```

### Pair 7 — §3 populated-rows paragraph, the uncovered IDs (replacement)

**OLD**
```
Six IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Four are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; and **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set. T-DATA-05 is why **Data tables** carries evidence without a ✓ — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified — and the three `T-SCN-` IDs are why **Content / scenario** does the same at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), Q29 there being read per ID.
```
**NEW**
```
Eight IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Six are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set; and **T-UI-03** and **T-UI-04**, written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at row 8's commit. T-DATA-05 is why **Data tables** carries evidence without a ✓ — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified — the three `T-SCN-` IDs are why **Content / scenario** does the same at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), Q29 there being read per ID, and T-UI-03 and T-UI-04 are why **UI** does the same at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303).
```

### Pair 8 — §4.5, the risk row's date stamp (replacement)

*Reduced and re-scoped* and *not retired* are true of this landing as they were
of the last; only the date moves.

**OLD**
```
**Reduced and re-scoped at 2026-08-03, not retired:**
```
**NEW**
```
**Reduced and re-scoped at 2026-08-04, not retired:**
```

### Pair 9 — §4.5, the green tally (replacement)

**OLD**
```
**50** of the 70 are green
```
**NEW**
```
**52** of the 70 are green
```

### Pair 10 — §4.5, the tail of the tally and the unclosed list (replacement)

**OLD**
```
and **1** at `6ccd40b`, where T-TURN-10 closed and completed row 5's acceptance set — so everything on the critical path but row 8 is evidence rather than schedule, **per acceptance ID as well as per row** now that T-TURN-10 has closed. **20 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; and the **16** in rows 8–10, which hold no code
```
**NEW**
```
**1** at `6ccd40b`, where T-TURN-10 closed and completed row 5's acceptance set, and **2** at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where T-UI-01 and T-UI-02 closed without closing row 8 — so every row on the critical path has now landed, row 8 last and on a partial pass, **per acceptance ID as well as per row**. **18 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; T-UI-03 and T-UI-04, which are written, unblocked and asserting, and for which no in-editor pass exists at row 8's commit, and which leave row 8 unflipped; and the **12** in rows 9–10, which hold no code
```

### Pair 11 — §4.7 register preamble, the T-CAP-05 exception (replacement)

Wrapped to the section's ~75 columns.

**OLD**
```
row 8 holds no code, so that
gate has not run — it asserts, and it is not green.
```
**NEW**
```
row 8 has since landed at
[`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303),
where that gate ran and passed under clang++ and MSVC both — on a fixture
configured with `captureTurns = 2`, a state the shipped scenario cannot
reach at N = 1 (Q4). It mints no numbered acceptance ID, so no §4.5 count
moves on its account, and whether T-CAP-05 itself closes on a fixture no
shipped map can reach is unruled (Q14).
```

### Pair 12 — §4.7 register, Q14's **Blocks** cell (replacement)

**OLD**
```
and row 8 holds no code, so that gate has not run and T-CAP-05 is not green; the kb victory table
```
**NEW**
```
and row 8 has since landed at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where that gate ran and passed under clang++ and MSVC both, on a fixture configured with `captureTurns = 2` — a state *Ferrum Crossing* cannot reach, since it ships N = 1 on Q4's ruling. Pass 1 of that build awarded partial credit toward `objectivesHeld` and the gate refused it, so this row's stated reading is asserted rather than only written. Whether T-CAP-05 closes on a fixture no shipped map can reach is not ruled here; the kb victory table
```

### Pair 13 — §4.11 preamble, row 8's clause (replacement)

Anchored on the clause alone. The bolded flipped-rows list above it is **outside
both blocks and unchanged**: row 8 landed and did not flip, so adding it to a
list of flipped rows would merge the two states this addendum exists to keep
apart. Wrapped to the section's ~75 columns.

**OLD**
```
and **row 8 is the critical path's remaining link**,
its dependency cell in the table below reading `5, 7` — both have landed,
row 7 on a partial pass that leaves its ledger row unflipped (§3).
```
**NEW**
```
and **row 8 was the critical path's remaining
link**, its dependency cell in the table below reading `5, 7` — both landed
before it. **Row 8 has since landed too**, at `7c36303`, on a partial pass
that leaves its ledger row unflipped, as row 7's does (§3): T-UI-03 and
T-UI-04 are the in-editor half and no in-editor pass exists at that commit.
```

---

## Build order

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |

Unchanged from §4.11's row 8. This addendum moves no dependency, no † mark and
no acceptance ID. Rows 9 and 10 are unchanged and unbuilt.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.11, the `T-UI-03, 04` † bullet | "**T-UI-03, 04** — in-editor Automation over widget bindings, where a Director reading the screen is a real check. T-UI-01/02 stay unmarked: they are headless queries, and T-UI-01 is what makes §2.11.3's forecast equal the resolution." | Append a cost line in the shape the other two bullets use: *Cost: row 8's ledger flip, since Q29 requires the full acceptance set at one commit.* | The T-DATA-05 and T-SCN-08/09/11 bullets each state their flip cost; this one does not, and as of `7c36303` it is the same cost and is realised rather than hypothetical. Not written as a pair: nothing in the bullet is false today, and adding a claim to a cut-line bullet is a Director edit. |
| §3 ledger table, the UI row's label | `UI` | Rename to §4.11's *UI binding*, or leave. | The same question the Content / scenario row raised at `9086d6a`, still unruled. Renaming a ledger row changes an identifier other sites may lean on, so Pair 5 leaves the label alone. |
| §4.7 Stub 8 (per-hex fields; Acceptance), §4.10 canonical state hash, §4.9 T-INT-05 | — | The four change requests filed with the row8-ui-binding addendum stand unchanged and unruled. | Row 8's build closed none of them: it left the per-factory build record, the income rate and §2.11.1's DONE bit absent from the snapshot rather than inventing fields for them. Restated as still-owed, not re-argued. |

## Open questions for the Director

1. **Does T-CAP-05 close?** `GATE-CAP-PARTIAL` ran and passed at `7c36303`, on a
   fixture configured with `captureTurns = 2`, and no shipped scenario can
   produce that state at N = 1. Row 7's precedent cuts both ways: T-SCN-08 does
   **not** close because part of its fixture set did not run, while its
   synthetic ceiling-refusal fixture (c) is counted as a run. Three sites state
   T-CAP-05's status in words — §2.8, §4.7's preamble and Q14 — and Pairs 1, 11
   and 12 leave all three saying the gate ran and the closure is unruled. §4.5's
   arithmetic does not carry T-CAP-05 either way, so nothing computable turns on
   this.
2. **"Playable via debug commands" (§4.4).** Row 8's landing re-opens it again,
   as the amended ruling says every system landing does. No pair here writes a
   met or unmet ruling. The precedent at rows 6 and 7 was that it was ruled met
   again and deliberately left unwritten; that is the Director's call each time,
   and this round takes it no further.
3. **Is `T-UI-04`'s buildlist a snapshot field or a query?** Stub 8 names the
   buildlist as derived from the four Stub-2 unit rows plus current `fameTotal`
   and does not say through which surface the UI reads it. The build offered
   neither rather than choosing. Same shape as the still-open question about the
   per-factory build record, and both now block a widget §2.11 specifies.
4. **Does Q29's per-ID reading extend to a †-marked ID whose harness does not
   exist yet?** Applied to T-UI-03/04 in Pair 4, it produces the same posture as
   T-DATA-05. Whether that is one rule or two — an ID written and unrun for want
   of an editor pass, versus one written and unrun for want of a map — is stated
   nowhere, and the two rows now sit side by side in §3.
5. **Whether §2's character count moving obliges a `kb/rules.md` re-sync.**
   Pair 1 is the only §2 edit, and neither `T-CAP-05` nor `GATE-CAP-PARTIAL`
   appears in `kb/rules.md`. The merge checklist's step 3 does not condition on
   identifier overlap, so this is the Director's call at merge time.

## Handoffs

- **ux-onboarding-designer** — nothing new. The three known-absent snapshot
  fields the build left absent still touch §2.11.5's BUILD pulse, §2.11.2's
  income rate and §2.11.1's DONE bit; those change requests were filed last
  round and are unchanged.
- **rules-designer** — Pair 1 edits §2.8's T-CAP-05 exception block. It changes
  no rule and no alias: only whether that ID's gate has run.
- **scenario-designer** — nothing. `GATE-CAP-PARTIAL`'s `captureTurns = 2`
  fixture is module configuration, not a map; no scenario file was authored or
  changed at `7c36303`.

## Grounding

Every OLD block was grepped against `source/gdd.md` (md5
`83899833551abbe9d4518e21fd771520`) as an exact string, including its line
breaks where it spans lines: **each matched exactly once**. Pair 3's OLD was
re-grepped at its extended span and matches once. Pairs 8, 9 and 10 land in the
one §4.5 cell; their spans are ordered and disjoint — the date stamp ends at
`not retired:**`, Pair 9 is the isolated tally phrase, and Pair 10 begins at
`and **1** at \`6ccd40b\``, with the untouched `18 / 9 / 9 / 6 / 7` enumeration
between Pairs 9 and 10.

**Insertion/replacement classification, re-derived from the current bytes rather
than carried forward:** substring test over each pair as it now stands — a NEW
block that contains its OLD anchor verbatim and contiguously is an insertion.
Only **Pair 4** does. Pair 3's extended NEW does **not** contain its extended
OLD, so Pair 3 is a replacement, as it was before the extension. **Twelve
replacements, one insertion.** The merge post-check should find Pair 4's OLD
present once and the other twelve absent.

Pair 4's anchor was taken long because the short form is ambiguous: *reporting a
harness that did not run is the exact failure this ledger exists to prevent*
occurs **twice** (§3's tracker line and §3's populated-rows paragraph); with the
`6ccd40b` clause prefixed it occurs once.

Eight `7c36303` citations are linked — Pairs 2, 5, 7, 10, 11 and 12 once each
and Pair 4 twice — and the link shape is copied from the `9086d6a` and `6ccd40b`
links already in §3 and §4.5 rather than composed. Pairs 1 and 13 cite no linked
sha: §2 carries no commit reference anywhere in the document (every sha
occurrence sits at line 1488 or later, verified by grep), and §4.11's preamble
cites shas bare.

Arithmetic is re-derived rather than copied. Green: 18 + 9 + 9 + 6 + 7 + 1 + 2 =
**52**. Unclosed: T-DATA-05 (1) + T-SCN-08/09/11 (3) + T-UI-03/04 (2) + rows
9–10 (**12**, being T-INT-01..05 and T-SAVE-01..07) = **18**; and 70 − 52 = 18.
The **16** the old text attributed to rows 8–10 is 12 + T-UI-01..04, so removing
the two that closed and the two that did not leaves 12 in rows 9–10.

**The driver's `snapshot` command, which Pair 4 names.** It prints §4.7 Stub 8's
view model, and `scenario snapshot` is the same command under the spelling row 7
advertised — at `9086d6a` that spelling refused on row 8's account and at
`7c36303` it does not. `GATE-DRV-12`, new at that commit, asserts the driver
holds no view model of its own: the same projection rebuilt through
`cpp_reference/Ui.h` matches field for field, and spending exactly one of a
unit's two per-unit flags shows one spent and one not. `GATE-DRV-01..12` is
12/12 under clang++ and MSVC both, and those IDs are still not `T-*` — the
driver is not a §4.7 stub and has no row in the ledger.

`source/gdd.md` supplies the rest: Q29 for the flip criterion Pair 4 applies per
ID; Q4 for N = 1 on *Ferrum Crossing*; Q14 for the partial-credit reading pass 1
broke; Q2 and Q26 for the two unwritten IDs Pair 4 distinguishes T-UI-03/04
from; §4.11's † bullet for T-UI-03/04 being the in-editor half; and the **Data
tables** and **Content / scenario** rows for the partial-pass shape Pairs 5, 6
and 7 follow.

Sites grepped document-wide and checked in the text that would falsify them,
not by identifier alone:

- `row 8` occurs at six lines: §2.10's off-critical-path bullet (unchanged — it
  states row 8 *depends on* row 7, which is still true), §3's tracker line
  (Pairs 3 and 4), §4.5's risk row (Pair 10), §4.7's preamble (Pair 11), Q14
  (Pair 12), and §4.11's preamble (Pair 13).
- `GATE-CAP-PARTIAL` occurs at **eight** lines — the first sweep reported five
  and its enumeration accounted for six, so both the figure and the list are
  corrected here. Lines 392 (§2.8's alias table row — it says only that T-CAP-05
  is not a `T-TURN-` ID), 400 (§2.8's exception block, **Pair 1**), 2395 and
  2405 (Stub 8's invariant list and Acceptance line — both describe what the
  gate asserts, not whether it has run), 2464 (§4.7's preamble, **Pair 11**),
  **2484 — §4.7 Q6's Assumption cell**, which records that T-CAP-05 has a gate
  of its own rather than an alias and that its gate home was ruled into Stub 8's
  snapshot on 2026-08-02, and makes no claim about whether that gate has run, so
  the landing does not falsify it — 2492 (Q14, **Pair 12**), and **2775 —
  §4.11's build-order row 8**, which lists `GATE-CAP-PARTIAL` in the row's
  acceptance set, which this addendum does not move.
- `*pending*` occurs at four lines: §1.7's revision-note row and §4.7's heading
  are dated records of a past state and do not move; §4.11's opening sentence
  names the eight rows *as at* that date and lists the flipped ones, which row 8
  does not join; §3's UI row is Pair 5.
- `critical path` occurs at **seventeen** lines (nineteen occurrences: 1511 and
  2501 carry two each), eighteen lines counting §4.11's capitalised *Critical
  path:* at 2824. The first sweep reported fourteen. The lines are 30, 71, 97,
  485, 1505, 1511, 1551, 1564, 1570, 1579, 1582, **1644**, **2359**, 2501,
  **2623**, 2752, 2838, plus 2824. The three the first count did not reach are
  bolded: 1644 is §4.7's cut-line paragraph (*no rules-correctness invariant on
  the critical path §4.11 states is ever in it*), 2359 is Stub 7's note that MCP
  stays off the critical path, and 2623 is §4.9's same note about editor-only
  tooling; none of the three says what has been built. Of the remainder, the
  three that assert row 8's position are Pairs 3, 10 and 13 (1511, 1582, 2752);
  30, 485, 1505, 1551, 1564 and 1579 place hotseat, row 7 or the MCP plugin off
  the path; 71, 97, 1570, 2501 and 2838 state the chain's shape or the Q23/Q20
  schedule ruling; and 2824 states the chain itself.
- §4.11's `| 8 | UI binding (Stub 8) | 5, 7 …` row states dependencies, the
  headless split and the acceptance IDs. None moved.
- §4.9's T-INT-05 and §4.10's hash list are untouched by this landing and remain
  the subject of change requests filed last round.
- §4.5's *against **9** verified ledger rows* is unchanged: row 8 does not flip,
  so the ✓ count stays nine.
