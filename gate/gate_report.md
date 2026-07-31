# Gate report — run `post-merge-2`

- **Audit target:** `source/gdd.md` itself (md5 `57bc80099a50193830e94ad1d8b191d6`, per `source/MANIFEST.txt`), plus `source/kb_rules.md` (md5 `0c1884f9e06619b35ae7608c824e8b93`) and `source/kb_setting.md` (md5 `b3e9e89daaef1cdeb333e3fb4368d1c0`). `source/MANIFEST.txt` is present; the run is not `sync-missing`.
- **Also audited as live merge sources:** `sections/ux.md`, `sections/scenario.md`, `sections/tech.md` (produced this stage) and `sections/rules.md` (carried, not re-issued — see the note under its area). Every one of these files declares a wholesale or in-place replacement of a merged GDD passage, so a stale line in them is a merge hazard, not a historical artifact.
- **Top-level verdict:** **BLOCK** — 20 violations across 7 areas.

| Area | Verdict | Violations |
|---|---|---|
| `source/gdd.md` §1.6 + §3 — Revision Notes + Provenance ledger | **BLOCK** | 2 |
| `source/gdd.md` §4.7 Open questions — the Q register | **BLOCK** | 2 |
| `source/gdd.md` §4.4 + §4.11 — Milestones + Build order | **BLOCK** | 1 |
| `sections/ux.md` | **BLOCK** | 5 |
| `sections/scenario.md` | **BLOCK** | 5 |
| `sections/tech.md` | **BLOCK** | 1 |
| `sections/rules.md` | **BLOCK** | 4 |

**Counting convention.** Where a defect exists both in the merged GDD and in the draft that produced it, it is filed once, against the file where the author must make the fix, and the report says where it is live today. Nothing below is double-counted.

---

## Status of the 17 violations from `post-merge-1`

**Sixteen are closed. One is closed in substance but re-opened by its own fix.** Every claim in the task prompt was checked against the document rather than accepted.

| # | Fix claimed | Verified |
|---|---|---|
| 1 | T-SCN-02 collision → T-SCN-05 added as a real invariant | **Closed.** T-SCN-05 exists, states the odd-r → axial round-trip, the adjacency match and the no-leak clause; Stub 7's `Acceptance:` reads `T-SCN-01..08`; §4.11 row 7 lists T-SCN-05 in the structural half. The formula in Shared conventions (`q = col − (row − (row & 1)) / 2`, `r = row`) is the correct odd-r conversion — I used it to path the maps below and it reproduces the authored adjacency. |
| 2 | Q8's invented clause deleted | **Closed.** Q8 now reads "T-FAME-02 and T-FAME-04 stay blocked until ruled, and they gate Stub 4, which §4.11 builds *before* the turn loop." §4.11 rows 4 and 5 confirm the ordering; Stub 4's Acceptance is `T-FAME-01..09`, so it is genuinely blocked. |
| 3 | Q-table header distinguishes stated readings from *unruled* rows | **Not closed.** The marker is applied inconsistently — see §4.7 area, violation 1. |
| 4 | §1.6 row 2 corrected to ten one-shots + two banners, three teachers | **Closed on the counts.** §2.11.6-C lists exactly ten one-shot strings plus the two cap-approach banners; §2.11.6's Philosophy lists exactly the three named teachers; §2.11.6-D has exactly twelve rows. The row's *other* clause ("scripted turn-1–3 guided opening") is now false for a different reason — see `sections/ux.md` violation 1. |
| 5 | §2.13.2 no longer quotes §2.8's struck "e.g. 20" | **Closed in the GDD** (`the §2.8 per-scenario cap, Stub 7 turnCap`). **Not carried into `sections/scenario.md`**, which still says "fixes §2.8's 'e.g. 20'" — filed. |
| 6 | §2.11.2 HUD mock now reads `+175/turn`, legal for four held objectives | **Closed, and the arithmetic checks.** 1 factory (+100) + 3 towns (3 × +25) = 175, which is exactly four objectives against the mock's `Obj. 4/8`, and 4/8 + 3/8 = 7 of 8 owned with one neutral — internally consistent, and consistent with §2.11.4's `Objectives 4/8 3/8` and §2.13.2's 4 factories + 4 towns. **Not carried into `sections/ux.md`**, which still mocks `3/6` and `+125/turn` — filed. |
| 7 | Six dangling CR pointers repointed; Q19 and Q20 filed | **Closed in the GDD.** §2.7 → Q5 and Q6; §2.11.1's `Z` row and its MOVED footnote → Q11; §2.13.1 → Q15; §2.8's delete-test → §1.6 row 5. Q19 and Q20 exist and their Blocks columns resolve. **Not carried into `sections/ux.md`, `sections/scenario.md` or `sections/rules.md`** — filed against each. |
| 8 | §4.10's overwrite-confirm UX marked unowned | **Closed.** §2.11.5's screen list ("title/menu, briefing, match, result") and §2.11.8's must-have list both exclude a save surface, so the "unowned" claim is true against the document it cites. |
| 9 | `kb_rules.md` reverted to `[unpinned]` on capture-N | **Closed.** The capture bullet reads `**[unpinned: exact N …]**` and no longer asserts per-scenario data. `kb_rules.md` is otherwise in sync with §2.3, §2.4, §2.7 and §2.8; the remediation touched no §2 rule, so no `kb-desync` arises from it. |
| 10 | §2.13.5's 0–6 factory swing and N = 10 | **Closed.** 6 factories + 4 towns = 10, against N = 8 on *Ferrum Crossing* (4 + 4, §2.11.4); the swing is correctly attributed to factories only, the domination win set. |
| 11 | Opening-capture reachability invariant + three-map lane table | **Closed, and the table is correct — I re-pathed all six lanes by hand.** See the verification block below. It nonetheless introduced two new defects — filed against `sections/scenario.md`. |
| 12 | §2.11.6-B beat 2 is a standing directive | **Closed mechanically** — it targets `guidedOpening.objective`, retires on the pip, and hard-expires end of turn 4. It introduced two new contradictions — filed against `sections/ux.md`. |
| 13 | Stub 7 gains `scenarioHash` append-at-tail policy, `guidedOpening`, T-SCN-06/07/08, Q21/Q22, §4.11 row 7 | **Closed.** All eight T-SCN IDs exist and every citation of them resolves (Stub 7, §4.11 row 7, Q21, Q22, the amended `Determinism:` and `Acceptance:` lines, §4.8's T-SCN-01 citation, Stub 8's T-UI-04, Q10, Q19). Row 7's split (structural `01..03, 05, 07` = five, priced `04, 06, 08` = three) sums to eight and matches the "three of its eight invariants" prose. One dangling pointer inside T-SCN-06 — filed against `sections/tech.md`. |

**Known-open items, judged as they stand:** the §4.4-vs-§4.11 schedule conflict and the §3 evidence links are filed as violations below, because neither is disclosed as a numbered open question and both make a false statement on the page. Title/lineage framing is unowned but asserts nothing false, so it is **not** a violation — it stays a Director item.

---

## Independent verification of §2.13.1's lane table

The table is now load-bearing for §2.11.6-B, T-SCN-06 and T-SCN-08, so I pathed every lane myself on the authored odd-r grids, counting the cost of every hex entered including the objective (Factory MoveCost 1, §2.3), Bridge-free, land-only.

| Map | Lane | GDD claim | Gate result |
|---|---|---|---|
| *Ferrum Crossing* | West (1,5) → (5,7) | 5 MP | **5 MP.** Axial distance 5; `(2,6) (3,6) (3,7) (4,7) (5,7)`, all cost 1. Confirmed. |
| *Ferrum Crossing* | East (9,3) → (6,2) | 5 MP, 4 hexes, one mandatory Woods | **5 MP.** Axial distance 4; every land-passable, Bridge-free neighbour of (6,2) is Woods — (7,2), (6,1), (6,3) — so the Woods hex really is mandatory. `(8,3)1 (7,3)1 (7,2)2 (6,2)1` = 5. Confirmed, and the earlier hex-vs-MP error is genuinely corrected. |
| *Longwater March* | West (1,3) → (4,2) | 3 MP | **3 MP.** `(2,2) (3,2) (4,2)`, all cost 1. Confirmed. |
| *Longwater March* | East (11,3) → (8,2) | 4 MP | **4 MP.** `(10,3) (9,3) (9,2) (8,2)`, all cost 1. Confirmed — and the 3-vs-4 asymmetry on a "Mirrored" map is real, which is the subject of a violation below. |
| *The Causeway* | West (1,3) → (3,2) | 2 MP | **2 MP.** `(2,3) (3,2)`; the (2,2) Mountain route costs 4 and is not the cheapest. Confirmed. |
| *The Causeway* | East (6,5) → (5,6) | 3 MP | **3 MP.** (5,6) is not adjacent to (6,5); the only common neighbours are (5,5) Woods and (6,6) Mountain, so the cheapest is `(5,5)2 (5,6)1` = 3. Confirmed. |

All six numbers are right, all six lanes are Bridge-free, and all six sit inside the 6 MP ceiling. The *Ferrum Crossing* "1 MP of slack, the tightest of the three" claim is also correct.

---

## `source/gdd.md` §1.6 + §3 — BLOCK (2)

### 1. `stat-drift` — §1.6 row 4 still cites a two-stage-stale register extent

> **Draft (§1.6 row 4):** "and where a rule was missing, it is filed as a numbered open question **(Q1–Q18)** instead of being invented."

> **Source (§4.7 preamble):** "state, the gate is parameterized on a numbered open question **(Q1–Q22**, Open questions below) — the Director rules, the gate then pins the ruling."

`sections/tech.md`'s Amendment 5 states it fixed "**the two** range citations that name the register's extent (`Q1–Q20` → `Q1–Q22`)". There are three. The third is §1.6 row 4, and it is still at Q1–Q18 — one stage behind even the pre-remediation value.

**Fix:** change §1.6 row 4's extent to `(Q1–Q22)`.

### 2. `unverified-claim` — the ledger asserts external auditability it does not have

> **Draft (§3 legend):** "**Evidence** cites the git commit + passing test IDs so any row is independently checkable."

> **Source (§3, same section):** "*(Commit `5ffa8d6` is present locally; a `git push` publishes the linked commit for external audit.)*"

Four rows carry **Agent-verified ✓** backed by four `github.com/jakemartin/stratocracy-crew/commit/5ffa8d6` links that do not resolve. The disclosure is honest but it is in a different paragraph from the claim, and the claim as written is false today; the same paragraph also says "this ledger is *checkable*". The document's own §3 rule is that a system is agent-verified only on evidence, not assertion.

**Fix:** push `5ffa8d6`, or strike "independently checkable" and mark the Evidence column locally-verified-pending-push until it is.

---

## `source/gdd.md` §4.7 Open questions — BLOCK (2)

### 1. `contradiction` — the new *unruled* marker names a row that is not marked and omits one that is

> **Draft (Open-questions preamble):** "**Rows marked *unruled* state no reading and block their gate outright** (Q4's interruption semantics, Q5's stacking, **Q6**, Q8, and Q9's target- and build-choice ties); those gates cannot be written until the Director answers."

> **Source (Q6's assumption cell):** "**Unpriced**, so no gate asserts it. The rules author recommends (c), with (b) as the fallback; either unblocks the T-CAP- suite immediately."

> **Source (Q20's assumption cell):** "**Unruled.** §4.4 stands as written; §4.11 records the conflict without resolving it. This is a scheduling decision, adjacent to the §4.4-vs-§4.11 critical-path question."

The fix created a term of art and then used it inconsistently in both directions. Q6 is enumerated as *unruled* but its cell never carries the marker and states a recommendation instead of a reading — so it fits neither half of the taxonomy the header just built. Q20 carries the marker verbatim and is not enumerated, and applying the header's stated consequence to it ("block their gate outright") would falsely declare T-INT-02 and T-SAVE-07 blocked, when §4.9 and §4.11 both treat them as live work items.

**Fix:** mark Q6 *unruled* (or restate its cell as a stated reading), and either drop Q20's marker or extend the header to say that a scheduling row blocks a milestone rather than a gate.

### 2. `dead-reference` — Q20 cites a question that carries no ID

> **Draft (Q20):** "This is a scheduling decision, adjacent to **the §4.4-vs-§4.11 critical-path question**."

> **Source (Open-questions preamble):** "Every gap found while writing the §4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and scenario-side rulings folded in here (Q14–Q20), and the two gaps found while gating §2.13.1's opening-capture invariant (Q21–Q22) **so that each question carries exactly one ID across the whole document**."

§4.11's closing paragraph makes the same citation. No Q in Q1–Q22 is the §4.4-vs-§4.11 critical-path question; the register's own exhaustiveness claim therefore fails.

**Fix:** file the critical-path conflict as a numbered Q and repoint both citations, or delete the citation.

---

## `source/gdd.md` §4.4 + §4.11 — BLOCK (1)

### 1. `contradiction` — §4.4's week 1 and week 2 schedule work that §4.11's dependency chain forbids

> **Draft (§4.4, wk 2):** "Engine presentation + UI wiring (select/move/attack) onto the wk-1 skeletons, the one scenario, **baseline objective-seeker AI** → **working vertical slice.**"

> **Source (§4.11 build order):** "| 6 | Opponent AI (Stub 6) | **5** | Yes | T-AI-01..06 + self-play smoke |" — and row 5 depends on row 4, "Capture & Fame economy (Stub 4)".

> **Source (§2.10 scope table):** "**multiple factories** (home-per-side + contested neutrals, ~4) + capture + Fame production *(these land wk **3**, not wk 1–2)*".

The chain is `1 → 3 → 4 → 5 → 6`, so the baseline AI cannot exist before the Fame economy, which §2.10 and §4.4 both place in week 3. §2.9's baseline AI has an **economy (build) phase**, which makes the dependency real rather than notional. §4.4's week 1 has the same problem: it lists "win" as week-1 work, and win/tiebreak is Stub 5, downstream of Stub 4.

This is the one item the task prompt names as deliberately untouched. It is still a contradiction on the page, and unlike the save/replay half of the same problem it is **not** filed as a change request — §4.11 discusses it in prose and Q20 points at it as though it were numbered.

**Fix:** re-sequence §4.4, or file the ordering conflict as a numbered open question so the conflicting schedule is a recorded proposal rather than an asserted milestone table.

---

## `sections/ux.md` — BLOCK (5)

### 1. `contradiction` — the guided window is bounded at turns 1–3 in three places and expires at turn 4 in two others

> **Draft (§2.11.6 intro):** "with a **guided opening**: **scripted directives across turns 1–3, then hands-off**."

> **Source (§2.11.6-B, beat 2):** "A capture pip appears — on whatever turn that happens; **hard-expires at end of turn 4**"

The standing-directive fix moved guidance into turn 4 but left the window statements untouched: §2.11.6's intro, §2.11.6-B's own heading ("**B. Guided opening (turns 1–3)**"), and §1.6 row 2 ("a **scripted turn-1–3** guided opening"). On turn 4 the strip can still be showing a directive, so "then hands-off" is false. §2.11.6-B's reconciling phrase ("one turn past the guided window") sits three paragraphs below the claim it contradicts, so an implementer reading the intro builds the wrong thing.

**Fix:** restate the window as turns 1–3 with a turn-4 backstop in all three places, or move the hard expiry to end of turn 3.

### 2. `contradiction` — beat 3 becomes unreachable in exactly the case beat 2 was made standing for

> **Draft (§2.11.6-B, after the table):** "the strip shows **one directive at a time, oldest outstanding first** … The strip disappears for good once all four beats have retired, and **unconditionally at the end of turn 4**."

> **Source (§2.11.6-D concept ledger):** "| Fame income & build | … | Income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | **Turn 3 directive completes: a bought unit stands on the board** |"

Beat 2 is older than beat 3. If beat 2 never retires it occupies the strip through turns 2, 3 and 4, and the strip is gone at the end of turn 4 — so beat 3 never displays at all, and the ledger's stated confirmation for the Fame-income concept can never occur. The prose covers early retirement ("a beat that retires early simply advances the next one") but not the late case the standing directive exists to handle.

**Fix:** state the queue's behaviour when beat 2 outstands — either let beat 3 pre-empt it, or extend the strip past turn 4 for beat 3 only — so the four-beat ledger stays reachable.

### 3. `stat-drift` — the HUD and scoreboard mocks are two revisions behind the merged section this file replaces wholesale

> **Draft (§2.11.4 mock):** "| Objectives 3/6      2/6   |" — and §2.11.2's "| Obj.   3/6   2/6  |" with "| +125/turn|"

> **Source (merged §2.11.4):** "**Objectives** as *X of N* over all factories + capturable towns (§2.8 criterion 2), N supplied by the scenario (§2.13) — **N = 8** on *Ferrum Crossing* (4 factories + 4 towns), as the mock shows."

Placement says this file "**Replaces §2.11 wholesale**" and the revision note says "every other line of this file is the stage-2 text as gated" — but the merged §2.11 is no longer the stage-2 text. A mechanical re-merge reverts N = 8 to N = 6 and `+175/turn` to `+125/turn`, both of which contradict §2.13.2's 4 factories + 4 towns.

**Fix:** carry the merged mocks and the `+175/turn` figure into this file.

### 4. `dead-reference` — the cap is treated as an unfixed example, but Q7 is RULED

> **Draft (§2.11.4):** "**Turn counter** against the cap, always. (`/ 20` uses **the §2.8 example value**; the cap must be fixed before this ships — change request below.)" — and the Change-requests row "| §2.8 Turn cap *(re-filed)* | \"the turn cap (e.g. 20 turns)\" | Fix the cap value |"

> **Source (§4.7 Q7):** "~~Turn cap value.~~ **RULED (this revision).** The cap is **per-scenario data**, stored in Stub 7's `turnCap`; *Ferrum Crossing* ships **20** turns. … §2.8, §2.11.4 and §2.13.2 now agree."

§2.8 no longer contains an example value to cite.

**Fix:** replace the wording with the merged citation of §2.13.2 and Stub 7 `turnCap`, and retire the §2.8 turn-cap change request.

### 5. `dead-reference` — undo still points at a change request instead of Q11

> **Draft (§2.11.1 input table):** "| **Z** | Undo move *(only if **the §2.5 change request** is accepted; otherwise unbound)* |" — and the state-machine footnote "Under the pending **move-undo change request** (re-filed below)".

> **Source (merged §2.11.1):** "| **Z** | Undo move *(only if **Q11 (§4.7)** is ruled to grant undo; otherwise unbound)* |"

**Fix:** repoint both the `Z` row and the footnote at Q11 (§4.7).

---

## `sections/scenario.md` — BLOCK (5)

### 1. `contradiction` — a "machine-verified" declared symmetry that neither stretch map can pass

> **Draft (§2.13.1, closing paragraph):** "Declared symmetry does not imply equal lane cost: an odd-r grid's row offset means a mirrored or rotated layout can still price the two seats' lanes 1 MP apart (*Longwater March*: **3 MP west, 4 MP east**)."

> **Source (§2.13.1, Validation invariants):** "factory count in the map file equals the count the domination check uses; **declared symmetry (mirror/rotation/none) is machine-verified**."

A mirror or rotation of the hex board is an isometry, so it preserves path cost exactly. A map whose two mirror-image lanes cost 3 MP and 4 MP is therefore **not** mirror-symmetric on the board — it is symmetric only in the ASCII column grid, which is a different object. I verified this directly: under a true axial mirror of *Longwater March* about its centre, the woods at (6,3) maps to (5,3) and (6,5) maps to (5,5), neither of which is woods; under a true axial 180° rotation of *The Causeway*, the town at (1,1) maps to (6,7) and not to (7,7), and the woods at (3,1) maps to the Water hex (4,7). Both stretch maps are naive offset-grid symmetric and hex-asymmetric.

This matters mechanically, not cosmetically. §4.7's Shared conventions and T-SCN-05 state "no authored file stores axial, and **no module code stores `(col, row)`**", and validation runs in the module on the loaded scenario — so the machine-verified symmetry check has nothing but axial coordinates to work with, and both declarations fail it. This file's own handoff to `tech-director` prescribes exactly that check ("The declared-symmetry check should compare in cube / axial coordinates, not by flipping the offset grid"), and so prescribes a check its own maps cannot pass.

**Fix:** name the coordinate space the symmetry check runs in, and reconcile — either redeclare *Longwater March* and *The Causeway* as offset-grid symmetric only (and say what that buys), or redraw them so the declaration is true on the board.

### 2. `invented-fact` — The Causeway's Infantry deployment hexes have no antecedent

> **Draft (§2.13.1 lane table):** "| *The Causeway* | **(1,3)** → **(3,2)**, **2 MP** | **(6,5)** → **(5,6)**, **3 MP** |"

> **Source (§4.7 Stub 7, T-SCN-07):** "`infantry` is **the hex of a starting placement of THAT side** whose unitId is the CanCapture row and whose isFlag is false"

§2.13.6 gives *The Causeway* a spec table, a layout, key coordinates and a match-length argument, but **no starting positions and no deployment rule** — unlike §2.13.2, which tabulates them, and §2.13.5, which inherits them ("Deployment mirrors Ferrum Crossing's pattern around each home"). So (1,3) and (6,5) are asserted as Infantry deployment hexes with nothing behind them, and T-SCN-07 cannot be evaluated against this map at all. The two hexes are not even constructed the same way: (6,5) is the *axial* 180° image of (1,3), whereas the offset construction used for the map's terrain would give (7,5).

**Fix:** state *The Causeway*'s deployment, and reconcile it with the construction used for the map's terrain.

### 3. `dead-reference` — §2.13.2's turn-cap cell still quotes §2.8's struck example

> **Draft (§2.13.2):** "| Turn cap | **20 turns** (**fixes §2.8's \"e.g. 20\"** for this scenario) |"

> **Source (merged §2.8):** "If neither flag has fallen by the turn cap (**20 turns** on the shipped scenario — the cap is per-scenario data, set in the scenario file's `turnCap` field, §2.13.2 and §4.7 Stub 7)"

This file's Placement promises that Director edits already applied to the master "are carried into this file **verbatim**, so a future re-merge cannot revert them". Two were carried; this one was not.

**Fix:** carry the merged cell text into this file.

### 4. `dead-reference` — §2.13.3 cites a local question number the merge retired

> **Draft (§2.13.3):** "capture at N=1 (fixed from §2.7's \"start N=1–2\" range — **Open question 2**) flips income the following turn."

> **Source (merged §2.13.3):** "capture at N=1 (fixed from §2.7's \"start N=1–2\" range — **Q4, §4.7**) flips income the following turn."

This file's own Open-questions block already maps its local numbering to the §4.7 IDs "so the two numberings never drift apart again"; §2.13.3 is the one place it still does.

**Fix:** repoint to Q4 (§4.7).

### 5. `contradiction` — the Director handoff diagnoses kb drift that no longer exists

> **Draft (Handoffs → Director):** "`kb_rules.md` is stale against GDD §2.3/§2.8 — its terrain table is **missing the Bridge and Factory rows** and its outcomes table is **missing territorial domination**."

> **Source (`source/kb_rules.md`):** "| Bridge | 1 | -10 | land,air | no | … | Factory | 1 | +15 | land,air | yes |" and "| decisive | **territorial domination** — control every factory on the map at the start of your turn | domination, factories, backstop |" and "**Both Town and Factory are capturable** (by Infantry only)."

The same handoff also states "`source/gdd.md` is one sync behind the master — it does not yet contain Q19, Q20", which `source/MANIFEST.txt` and the Q register both contradict. A Director working merge-checklist step 3 from this handoff would re-parse a KB that is already correct and skip whatever is actually owed.

**Fix:** delete both stale status claims.

---

## `sections/tech.md` — BLOCK (1)

### 1. `dead-reference` — T-SCN-06 points at a note that was never placed in the GDD

> **Draft (Amendment 3, inside the replacement block for T-SCN-06):** "Asserting the existential over the NAMED hex is deliberate — **see the note above the stub**."

> **Source (the merged GDD immediately preceding Stub 7):** "Acceptance: T-AI-01..06, plus a self-play smoke run: N headless AI-vs-AI games all terminate at or before the cap with a valid result tier." — the last line of Stub 6. Nothing else separates Stub 6 from Stub 7.

The reasoning this points at ("Written the other way — find any qualifying hex, then compare it to the named one — the validator can pass a map whose qualifying lane belongs to a different unit…") lives only in tech.md's Amendment-3 commentary, which was never part of the replacement text. The remediation that closed one dead reference opened another, inside the very invariant it added.

**Fix:** add the note to §4.7 above Stub 7, or inline the two-sentence justification into T-SCN-06 and drop the pointer.

---

## `sections/rules.md` — BLOCK (4)

*Not re-issued this stage; it is the stage-2 draft. It is gated anyway because its Placement reads "Replaces **§2.1–§2.10 and §2.12 in full**", which makes every stale line in it a live revert risk, and because §2.7 and §2.8 are the sections `kb_rules.md` is parsed from.*

### 1. `contradiction` — it proposes reversing a ruling the document now depends on

> **Draft (Change requests):** "| §2.8 | \"the turn cap (e.g. 20 turns)\" | **Pin the cap: \"the turn cap (20 turns)\"** | … An \"e.g.\" cap is not machine-checkable. |"

> **Source (§4.7 Q7):** "**RULED (this revision).** The cap is **per-scenario data**, stored in Stub 7's `turnCap`; *Ferrum Crossing* ships **20** turns."

`kb_rules.md` now states outright "Do not describe the cap as a global constant."

**Fix:** retire the change request.

### 2. `dead-reference` — §2.7 and §2.8 still point at change requests and local question numbers

> **Draft (§2.7):** "(e.g. a Tank kill = +150 — **see change request** to make this exact); an **undamaged strike** … pays a small bonus (**see open question 1**)"

> **Source (merged §2.7):** "(e.g. a Tank kill = +150 — **see Q5, §4.7**, to make this exact); an **undamaged strike** … pays a small bonus (**see Q6, §4.7**)"

§2.8's delete-test block has the same defect ("The one piece that failed the test … is cut (**see change request**)" against the merged "(§1.6 row 5)"), and this file's Open questions 1–4 duplicate Q6, Q14, Q2 and Q4 under local numbers.

**Fix:** repoint all of them at their §4.7 IDs and drop the local numbering.

### 3. `dead-reference` — three change requests quote text the GDD no longer contains

> **Draft (Change requests):** "| §2.10 | **\"5 terrains\"** (IN row) | \"6 terrains + the Factory tile\" |" — plus the §1 "four units, five terrains" row and the §2.4 "(Pillar 4)" row.

> **Source (merged §2.10):** "Grid; 4 units; **6 terrains + the Factory tile**; move + attack; …" — §1 reads "six terrains + the capturable Factory tile" and §2.4 reads "(Pillar 3; PX-3)".

All three were merged. A Current-text column that quotes text the GDD does not contain cannot be adjudicated.

**Fix:** drop the three merged rows.

### 4. `contradiction` — all four kb-drift claims in the Director handoff are now false

> **Draft (Handoffs → Director):** "`kb_rules.md` (a) terrain table is missing the **Bridge** and **Factory** rows and states \"only Town is capturable\" … (b) victory table omits §2.8's territorial domination … (c) the gate-verified **Repair** rule … is absent … (d) kb says \"Move cost is per land unit\" where the GDD says per movement class."

> **Source (`source/kb_rules.md`):** "Notes: Move cost is **per movement class** … **Both Town and Factory are capturable** (by Infantry only). **Factory** is also the build/spawn point and a repair point (§2.7)." — plus the full Repair bullet in the economy block and the territorial-domination row in the outcomes table.

**Fix:** delete the handoff.

---

## Verdict

**BLOCK.** Sixteen of the seventeen `post-merge-1` violations are genuinely closed, and the three claims I was asked to test hardest all survive scrutiny: `+175/turn` is legal against the mock's own `4/8` (1 factory + 3 towns), the T-SCN-01..08 set is complete and every citation of it resolves, and §2.13.1's three-map lane table is correct in all six cells — I re-pathed each lane on the authored grid and the numbers, the Bridge exclusions and the "1 MP of slack" claim all hold. What blocks the merge is that four of the fixes did not finish the sweep they started, and one raised a defect of its own: the *unruled* marker in the Q register names a row it never marks and omits one it does; the standing-directive change left three statements still bounding the guided opening at turns 1–3 and, worse, left beat 3 unreachable whenever beat 2 hangs; T-SCN-06 now cites a note that exists in `sections/tech.md` but not in the GDD; and the §4.4-vs-§4.11 ordering conflict is still asserted as a milestone table rather than filed as a numbered question. Underneath all of that sits the structural problem this run has to name: **`sections/ux.md`, `sections/scenario.md` and `sections/rules.md` all declare wholesale replacement of §2.11, §2.13 and §2.1–§2.10, and none of them is a superset of what is merged today** — re-merging any of them reverts the cap ruling, the N = 8 scoreboard, the Q-pointer repointings and three already-closed change requests. The single most serious finding is the symmetry contradiction in §2.13.1: *Longwater March*'s own measured 3 MP / 4 MP lane split is proof that the map is not mirror-symmetric on the hex board, and since T-SCN-05 forbids the loaded state from holding `(col, row)`, the "machine-verified" symmetry check can only run in axial — where both stretch maps fail their declared symmetry. Before merge: close the five source-document violations (§1.6's Q1–Q22 extent, §3's evidence links, the Q-register marker, Q20's ID-less citation, the §4.4/§4.11 ordering), have `scenario-designer` rule the symmetry coordinate space and state *The Causeway*'s deployment, have `ux-onboarding-designer` fix the turn-4 window and the beat-3 queue, have `tech-director` land or inline T-SCN-06's missing note, and re-baseline all four `sections/` files against the current master so that a re-merge is idempotent rather than destructive.
