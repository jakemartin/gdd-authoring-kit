# Gate report — run q31-boxed-in-build-3

Source: `source/gdd.md` (md5 `ff680be5b9c4467dc1ac846244926c08`, per
`source/MANIFEST.txt`). Sections reviewed: `sections/rules_q31-boxed-in-build.md`,
`sections/ux_q31-boxed-in-build.md`, `sections/tech_q31-boxed-in-build.md`.
This is a fresh, full re-verification of all three files, not a diff against
runs 1–2.

## sections/rules_q31-boxed-in-build.md — PASS

All four OLD blocks were checked verbatim against the master:

- P1 (§2.7 build-and-spawn bullet, lines 246–251 of the master) — exact match.
- P2 (§4.7 Q31 register row, line 2658) — exact match, including the
  "Blocks" and "Assumption in force" cell text.
- P3 (§4.7 Q8 row's stale Q31-status sentence, embedded in line 2635) —
  exact match.
- P4 (§4.7 preamble ruled/open tally, lines 2611–2614) — exact match. The
  17→18 ruled / 17→16 open arithmetic and the open-row list (removing Q31
  from "Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31 and Q32") both check: the prior
  list is 3+10+4=17, the new list is 3+10+3=16.

No stat-drift, no invented facts, no dead references. Grounding claims
(Q8(c), the ruled/open convention at Q29/Q33/Q34, the register's own count
paragraph) all check against the cited rows. Handoffs to `ux-onboarding-designer`
and `tech-director` correctly identify the two sites this author left
untouched, and both of those sites are in fact picked up by the other two
drafts this round. No violations.

## sections/ux_q31-boxed-in-build.md — PASS

Pair 1's OLD block (§2.11.5 production-menu footer/button-state passage,
line 704 of the master) now quotes §2.11.5's own text verbatim — confirmed
character-for-character against the master, including the `spawnBlocked`/
`buildWaiting` sentence. This resolves run 2's placement-collision finding;
no other draft targets this anchor, so there is no collision in the
aggregate either.

The Check-results table's five swept, no-pair-needed sites were each
verified against the master: the §2.7 "player cannot currently reach"
sentence, §4.7 Stub 8's field note, §2.11.8's "grey/shortfall/boxed states"
phrase (line 798), the §4.7 preamble tally, and the §4.7 provenance-chain
sentence (line 2561) — all quoted exactly as they appear in `source/gdd.md`.
Grounding claims (the Q31 ruling, §2.7's waiting-build rule, the existing
production-menu mockup, the snapshot fields) are each traceable to a cited
GDD location. No violations.

## sections/tech_q31-boxed-in-build.md — PASS

Pair 1's OLD block (§4.7 Spec Stub 8's `buildWaiting`/`spawnBlocked`
per-factory note, lines 2436–2440) is an exact match, whitespace and all.

The Checks section's count is now correct: `Q31` occurs exactly **twice**
inside the Stub 8 fence (lines 2436 and 2439), both inside the passage this
pair replaces — verified by reading the fence's full extent (lines 2379–2547,
confirmed by locating the opening ` ``` ` and closing ` ``` ` at those exact
line numbers). `AI-only path` occurs once in that same span, matching the
draft's claim. The document-wide tally of six `Q31` occurrences reconciles:
two inside the fence (both edited) plus four outside it (line 250, §2.7;
line 2561, the provenance-chain paragraph; line 2613, the preamble tally
list; line 2658, the register table row) — all four confirmed present and
correctly attributed to their owning authors, none of them edited by this
draft. This resolves run 2's invented-fact finding.

The `T-UI-05` grounding citation (`sections/tech_t-ui-05-built.md`, Pair 5
and Pair 15) points to a file that exists in `sections/` and is consistent
with the master's own `T-UI-05` material (lines 2398, 2507, 2534–2547) — not
a dead reference. No violations.

## Cross-section checks

- **Placement collisions:** none. The three drafts target three disjoint
  anchors (§2.7 + §4.7 register rows; §2.11.5; §4.7 Stub 8), and each
  author's Handoffs/Check-results section correctly names the other two
  sites as out of scope for itself.
- **kb-desync:** none. `kb_rules.md` (line 66) carries only the basic
  build-and-spawn sentence and does not carry the "player cannot reach the
  waiting case" / "AI-only path" claim this ruling retracts, so the ruling
  does not make the KB wrong.
- **Voice / format:** all three files carry the required headings
  (Placement, Draft, Change requests, Open questions, Grounding, plus extra
  Handoffs/Checks sections) and are written in the GDD's declarative,
  present-tense register.

## Verdict

**PASS.** All three drafts are cleared to merge as exact OLD→NEW pairs
against `source/gdd.md` at `ff680be5b9c4467dc1ac846244926c08`. Before merge,
the Director should apply the pairs in the order rules → ux → tech (their
anchors do not overlap, so ordering is not load-bearing, but Stub 8's
line numbers will shift once §2.7/§4.7 register edits land above it, so
tech's pair should be applied against the pre-edit line numbers or
re-located by anchor text rather than by line number after the first two
pairs are in).
