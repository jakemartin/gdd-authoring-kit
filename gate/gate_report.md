# Gate report — run `post-merge-6`

- **Audit target:** `source/gdd.md` itself (md5 `68a57cf71d15290685e654f2e3fdcbac`, per `source/MANIFEST.txt`, matching the md5 named in the task), plus `source/kb_rules.md` (md5 `0c1884f9e06619b35ae7608c824e8b93`) and `source/kb_setting.md` (md5 `b3e9e89daaef1cdeb333e3fb4368d1c0`). `source/MANIFEST.txt` is present; the run is not `sync-missing`.
- **`sections/`:** 13 `.md` files, all inert (see the `sections/` area below). No draft was produced this run, so there is no placement to collide.
- **Top-level verdict:** **PASS** — 0 violations across 12 areas.
- **Carried forward:** nothing. Every area was re-derived from this document state. The four `post-merge-5` findings were re-checked from the document's own text, not accepted on the orchestrator's report, and each area that passed last run was re-swept rather than assumed.

| Area | Verdict | Violations |
|---|---|---|
| §1, §1.5, §1.6 | **PASS** | 0 |
| §2.0–§2.10 | **PASS** | 0 |
| §2.11 (UI/UX + onboarding) | **PASS** | 0 |
| §2.12–§2.13 (lineage, scenario & map design) | **PASS** | 0 |
| §3 (AI architecture + provenance ledger) | **PASS** | 0 |
| §4.1–§4.5 | **PASS** | 0 |
| §4.6 (token budget) | **PASS** | 0 |
| §4.7 (gate plan + open-question register) | **PASS** | 0 |
| §4.8–§4.11 | **PASS** | 0 |
| `source/kb_rules.md` | **PASS** | 0 |
| `source/kb_setting.md` | **PASS** | 0 |
| `sections/` | **PASS** | 0 |

No violations are filed this run, so this report is a record of what was checked and how each prior finding was closed.

---

## The four `post-merge-5` remediations, re-derived

### 1. §2.13.1 fact 1 — repointed to Q26. **Closed.**

Current text (§2.13.1, symmetry note, fact 1):

> Whether a horizontal `mirror` therefore becomes a declarable value alongside `rot180`, with an odd-row-count precondition, is open as **Q26** (§4.7), which owns that question; no map in the set declares one today.

Against §4.7's Q24 row: *"(**Whether a third value should be admitted for the horizontal mirror is Q26**, which owns that question — this row asks only about the narrowing.)"* — now consistent.

**The symmetry story is single-voiced.** All seven sites that speak about declarability were read together and agree: §2.13.1's validation-invariants bullet (*"is **Q26**, which owns that question in full"*), fact 1 (above), fact 2 (even-row precondition, correctly filed to Q24 at Stub 7 / T-SCN-09), §2.13.5's and §2.13.6's Symmetry rows (both say the vertical mirror exists at no dimension and the horizontal one only on odd H, citing §2.13.1 and declaring `rot180` on 8 rows), Stub 7's `symmetry` field (narrow by scope, "Q26 asks which one is intended"), the reserved T-SCN-10 ("Blocked on Q26"), and the Q24/Q26 rows themselves. Q24 now asks only about the narrowing; Q26 owns declarability. No site implies otherwise.

Both geometry proofs were re-derived independently, not read: μ(q, r) = (q + r − (H−1)/2, H−1−r) is integer-valued exactly when H is odd and is a true isometry (it sends (dq, dr) → (dq+dr, −dr), permuting the three terms of the axial metric); ρ(q, r) = (W − H/2 − q, H−1−r) has a half-integer constant on odd H, and the 9 × 9 case does put (1,1) at column 6.5.

### 2. §4.6 — the whole chain re-derived from printed inputs. **Closed. No fourth fault found.**

The corrected parenthetical now reads *"it sat $1.005 above what its own stated inputs produced ($267 − $265.995; the often-quoted $1.24 came from the retired $1.03 delta)"*. $267 − $265.995 = **$1.005** ✔, and the provenance claim checks: 315 × $0.69 + 47 × $1.03 = $217.35 + $48.41 = $265.76, and $267 − $265.76 = **$1.24** ✔ — so the retired figure is correctly attributed and is named, not used. This does not conflict with §4.6-A's *"$1.035 is the only escalation delta used anywhere in §4.6"*: no computation in the section runs on $1.03.

Every figure in §4.6, recomputed from the two rate lines and the task count:

- Per-task tokens 100k + 200k + 45k = 345k ✔; Sonnet $0.20 + $0.04 + $0.45 = **$0.69** ✔; Opus $0.50 + $0.10 + $1.125 = **$1.725** ✔; delta **$1.035** ✔.
- 5 × 6 × 7 = **210 tasks** ✔; 210 × $0.69 = $144.90 ≈ $145 ✔; 210 × 345k = 72.45M ≈ 72M ✔.
- 15% of 210 = 31.5 → **32** ✔; 32 × $1.035 = **$33.12** ✔; subtotal $144.90 + $33.12 = **$178.02** ✔, and the round-first path $145 + $33 = $178 ✔.
- Substitution alternative: 32 × $1.725 = $55.20 ✔; $144.90 + $55.20 = $200.10 ≈ $200 ✔.
- Part B: 2.5k + 1.5k + 0.4k = 4.4k ✔; Haiku $0.0025 + $0.00015 + $0.002 = $0.00465 ≈ $0.0047 ✔; 20 turns → 88k and $0.093 ≈ $0.09 ✔; 200 matches → 17.6M and $18.60 ≈ $19 ✔; Sonnet intro $0.0093/turn → $37.20 ≈ $37 ✔; Sonnet standard $3/$15 with cache at 0.1× → $0.01395/turn → $55.80 ≈ $56 ✔.
- Headline: 72.45M + 17.6M = 90.05M ≈ 90M ✔; $178 + $19 = $197 and $178 + $37 = $215 ✔ (the $197–$215 band); 210 × 1.5 = **315** ✔; 15% of 315 = 47.25 → **47** ✔; 315 × $0.69 + 47 × $1.035 = $217.35 + $48.645 = **$265.995 ≈ $266** ✔; $266 + $19 ≈ $285 ✔; $266 + $37 ≈ $303 ✔, and $303 is indeed the largest figure the section produces.
- The $267 root cause is correctly diagnosed: 1.5 × the rounded $178 = $267 exactly ✔.

**There is no fourth fault hiding.** Two judgment calls are recorded rather than filed: the phrase *"the second arithmetic fault this table has surfaced"* counts the $225 double-application and the $267 headline, and does not count the $1.24 residue — defensible, since $1.24 was a mis-measurement of the second fault rather than a third one, and no other figure in the document states a fault count to contradict. And naming the retired $1.03 is a provenance statement, not a use.

### 3. Q27's Blocks column — the new text is true. **Closed.**

Current text (§4.7, Q27, Blocks): *"Nothing today, and nothing in §4.7: no stub or `T-` ID gates the directive strip, and Stub 7 deliberately keeps the guidance layer out of Stub 8's snapshot."*

Checked exhaustively, since the instruction was that a false negative here is as bad as the old dead reference:

- **Every `T-` ID in the document** was enumerated against the strip: T-HEX-01..07, T-MOVE-01..07, T-FAME-01..09, T-TURN-01..09, T-AI-01..06, T-SCN-01..10, T-UI-01..04, T-DATA-01..06, T-CAP-01..08, T-INT-01..05, T-SAVE-01..07, T-COMBAT/T-REPAIR @ `5ffa8d6`. None asserts anything about strip behavior, beat ordering, the last-call tag, or End Turn inertness. Stub 8's four invariants are forecast, reachable highlight, scoreboard binding and production menu.
- **Stub 7's `guidedOpening` field** confirms the second clause verbatim: *"marked/locked is presentation state, not rules state, so it stays out of the Stub-8 snapshot."* Stub 8's snapshot field list carries no guidance field.
- The one thing that *does* touch the guided opening from §4.7 is **T-SCN-06/07/08**, which price and name the lane (`guidedOpening.infantry` / `.objective`) the strip reads. That is the scenario **data**, not the strip: §4.11's *"the §2.11.6 guided opening ungated for however long movement slips"* is about those lane invariants, and it remains true alongside Q27's narrower claim. A Q27 ruling in either direction moves no `T-` ID, which is what the Blocks column asserts.
- The rest of the row is faithful: the question restates §2.11.6-B's beat-1a text including the hover string `Move the marked Infantry first.`; the internal-to-§2 dependency it names is real (§2.11.6-B: *"Turn 1 is identical in all three columns because 1a and 1b cannot outlive it"*); and the stated fallback matches the assumption column.

### 4. §3's evidence links and the "independently checkable" claim — **supported on the document's own terms.**

The old parenthetical conceded the commit was local-only and contradicted the ledger's auditability claim in the same section; that contradiction is gone. The replacement — *"(Commit `5ffa8d6` is published: it is an ancestor of `main` at [`2fcbf32`](…/commit/2fcbf32) on the public remote, so every link above resolves and the ledger's 'independently checkable' claim is testable by clicking it.)"* — is a checkable assertion rather than a concession, and nothing in `source/` contradicts it. I have no network access, so I judge only what the gate can judge: the document no longer undercuts itself, and the claim it now makes is falsifiable by the reader it is addressed to, which is the property the legend promises.

**On over-claiming, judged fresh rather than treated as closed.** I do not file it, and here is the reasoning rather than a bare ruling. The concern is that four Verified rows rest on one module and one commit. The section discloses exactly that, in the sentence immediately under the table: all four rows are named as coming from the same Assignment-3 headless Combat module at `5ffa8d6`. The row arithmetic is honest — T-COMBAT-01..10 (10) + T-REPAIR-01..07 (7) = the claimed **17/17**, with T-COMBAT-09..10 correctly shown as a *subset* cited by the Type-effectiveness row rather than as additional evidence, and §4.8's "16/16 pairs" is the pair count inside T-COMBAT-09, not a second test ID. Eight rows remain `*pending*` and map one-to-one onto Stubs 1–8 and §4.11 rows 1–8. The ledger's own rules ("human work counts as human") and §1's framing ("supporting evidence, not the pass/fail bar") keep the claim scoped. Two residual weaknesses are worth the Director's eye but are not violations under any type: the **Test suite** row's evidence is the test file certifying itself, and bar (b) of "agent-verified" — human review-gate sign-off — is asserted per-ledger, not cited per-row. Neither is a claim without a commit and passing test IDs, which is what `unverified-claim` covers.

---

## Also verified this run (the orchestrator's four checks, plus a full re-sweep)

**The register, Q1–Q27.** Each ID is defined exactly once, in ascending order, one row each. The preamble's provenance ranges (Q1–Q10, Q11–Q13, Q14–Q20, Q21–Q22, Q23, Q24–Q25, Q26, Q27) partition 1..27 with no gap and no double filing. **Every Q citation elsewhere in the document resolves to the right question** — all 40-odd sites were checked individually, including the ones most likely to rot: §2.7's Q5/Q6, §2.11.1's two Q11 sites, §2.11.6-B's Q27, §2.13.1's Q24 (constraints) and Q26 (declarability), §2.13.1's Q21 pair, §2.13.5's Q19, Stub 7's Q7/Q24/Q26, T-SCN-06's Q4, T-SCN-07's Q22, T-SCN-08/09's Q25, T-SCN-10's Q26, §4.8's Q2, §4.10's Q12, §4.11's Q20. Ruled rows (Q7, Q23) are cited as rulings, not as open blocks.

**Pinned extents.** One remains and it is currently accurate: §4.7's preamble, *"parameterized on a numbered open question (Q1–Q27, Open questions below)"*. It is correct against the register today, so it is not a violation — but it is the one citation in the document that goes stale the moment a Q28 is filed, and it is the class of thing the last three runs have been de-pinning. Reported, not filed. All test-ID extents reconcile with their listings, including §4.11's split of T-SCN into a structural half (01..03, 05, 07, 09) and a priced half (04, 06, 08), and the two reserved IDs (T-MOVE-07 on Q2, T-SCN-10 on Q26) that are deliberately unwritten.

**§2.11.6-B, all three branches, re-traced cell by cell** from the two selection rules rather than read off the table. Turn 1 is forced in every column (1a retires on the move, hands to 1b, whose retire condition is the turn boundary). Common: T2 beat 2 rule 1 → pip; T3 beat 3 rule 1; T4 beat 3 rule 2, tagged. Wandered: T2 beat 2 holds and yields; T3 beat 3 rule 1 (beat 2 has already held); T4 rule 2 selects beat 2, tagged, with the "How to read a cell" convention correctly resolving the turn-3-pip sub-branch to beat 3. Fast lane: beat 2 retires on the turn-1 pip without ever holding the line; T2 beat 3 rule 1; T3 rule 2 **untagged**; T4 rule 2 tagged. The twice/once/never enumeration is exhaustive over pip timing; the "no beat expires unheard" and "never quiet before end of turn 4" guarantees both hold (rule 2 has no exit, and the all-four-retired state is first reachable at end of turn 1 only in the fast lane with a turn-1 build, affordable at 200 Fame ≥ Infantry 100); the §2.11.6-D ledger's "turn 2 or turn 3 in every branch" is true (T3 / T3 / T2). Beat 1a's row carries the **Q27** citation and the register row matches it.

**§2.13, re-counted rather than re-read.** All three ASCII maps were counted hex by hex against their distribution lines — Ferrum 75/8/2/4/2/4/4 = 99, Longwater 86/4/4/0/0/4/6 = 104, Causeway 52/4/2/6/2/2/4 = 72 — and every key coordinate matches the glyph at its cell. Every ρ-pair in §2.13.5 and §2.13.6 holds under the stated ρ, including all four starting-position pairs on each map. All six lane costs re-price from §2.3 costs and odd-r adjacency: Ferrum 5/5 (the East lane's Woods ring hex is genuinely mandatory — every Bridge-free approach to (6,2) is Woods), Longwater 4/4, Causeway 3/3 with the two-hex Mountain alternative at 4 MP, giving the claimed 1, 2 and 3 MP of slack. Home separations 8 / 10 / 6 and the N = 8 / N = 10 denominators reconcile, as do the 550-Fame producible force and the 83% / 76% Plains figures.

**Cross-document consistency spot-checks that recompute:** §2.11.3's forecast (round(10 × 1.0 × 1.0 × 0.8) − 5 = 3, counter 0 out of range) against §3's formula; §2.11.5's production mock at a 250-Fame pool (`need 50` on the Tank); §2.11.2/§2.11.4's scoreboard mocks against each other (`+175/turn` = 1 factory + 3 towns = the 4/8 objectives shown; chevron on the enemy at 600 vs 450 per "higher wins"); §2.13.3's ~45 s/turn → 10–13 minutes once paced AI playback is counted, inside §1's envelope; the terrain count reconciled across §1, §2.3, §2.10 and the kb; the Q23 schedule holding at all four sites (§1, §2.10, §4.4, §4.11).

**`kb_rules.md` and `kb_setting.md` — no `kb-desync`.** Unit table, terrain table (including Bridge's −10% and Water's land-impassability), economy block and victory block compared field by field against §2.3, §2.4, §2.7 and §2.8: all values match. The `[unpinned]` markers still align with the register's unruled rows (Q4 capture N and interruption, Q5 exact awards, Q6 undamaged strike). The turn-cap block correctly states per-scenario data with *Ferrum Crossing* at 20 (Q7). §2.13.5's six factories do not desync the kb's hedged "typical ~4 factories total" under Q19. `kb_setting.md`'s tone bible governs §2.11.4's five result lines correctly — present tense, ≤ 30 words, faction voice only on the result screen, neutral system voice on the draw lines, no banned register.

**`sections/`.** All 13 files are inert and correctly headed: three superseded drafts (`ux.md`, `scenario.md`, `rules.md`, each carrying "⛔ SUPERSEDED — DO NOT RE-MERGE") and **ten** applied addenda (`tech.md`, `tech_post-merge-2..5`, `ux_post-merge-2..4`, `scenario_post-merge-2..3`, each carrying "✅ APPLIED ADDENDUM — DO NOT RE-APPLY"). Each file carries the required Placement / Draft / Change requests / Open questions / Grounding headings. No live draft, so no placement collision is possible. Two bookkeeping notes, neither a document defect: the task states **eleven** files as three drafts plus eight addenda — the actual count is **thirteen**, three plus ten; and the `post-merge-5` report recorded `sections/` as "empty but for `.gitkeep`", which is not true of the directory as it now stands. Nothing in `sections/` regressed, but the inventory the orchestrator is tracking is off by two addenda and should be corrected before it is used to decide anything.

---

## Known-open items, judged as they stand

Not violations; each is correctly carried rather than silently resolved.

- **Q20, Q21, Q22, Q24, Q25, Q26, Q27 unruled.** Each states a conservative reading that is what ships and what the gates assert, per the register's stated convention, so a later ruling loosens rather than invalidates. Q4's interruption semantics, Q5's stacking, Q6, Q8 and Q9's target/build ties correctly state *no* reading and block their gates outright, and the register's own list of those blocked rows matches the rows themselves.
- **§3's ledger at four built, eight pending.** The eight pending rows map one-to-one onto Stubs 1–8 and §4.11 rows 1–8. No row claims a status its evidence column does not carry.
- **Title / lineage framing remains unowned.** It belongs to a `narrative-designer` that does not exist in this kit, and no agent in this kit has taken it — correctly, since taking it would be `scope-breach`. It stays a Director item.

---

## Verdict

**PASS.** All four `post-merge-5` violations are closed at their sites and closed correctly, and no new defect was introduced by the remediation — which is the failure mode the last two rounds exhibited and the reason every neighbouring claim at each edit site was re-derived rather than re-read. §4.6's full chain reproduces from its printed inputs end to end with no fourth arithmetic fault, including the two figures the corrected parenthetical now names; Q27's Blocks column is true against every `T-` ID and every stub in the document; §2.13's symmetry story speaks with one voice at all seven sites, with Q24 narrowed and Q26 owning declarability; and §3 no longer contradicts its own auditability claim, which I judge supported on the document's own terms while recording, for the Director rather than as a violation, that all four Verified rows rest on one module and one commit and that the Test suite row's evidence is the test file itself. Nothing blocks merge. Two items should travel with this record and be fixed by the Director, not by an author: `sections/` holds thirteen files, not the eleven the run assumed, and §4.7's preamble still carries the one live pinned extent, `Q1–Q27`, which is accurate today and stale the moment a Q28 is filed.
