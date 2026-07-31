# Gate report — run `stage-2` (re-run)

- **Master:** `source/gdd.md` (md5 `4cdcff7ad4abbb3c93ad0036ead04faf`, per `source/MANIFEST.txt`)
- **Sections checked:** `sections/rules.md`, `sections/ux.md`, `sections/scenario.md`, `sections/tech.md`
- **Top-level verdict:** **PASS** (4 sections pass, 0 violations)
- **Context:** re-run after `ux-onboarding-designer` and `tech-director` corrected the four violations filed by the previous stage-2 gate run. Both corrections are verified below; `rules.md` and `scenario.md` are unchanged and were re-audited in full, not carried forward on the prior verdict.

---

## sections/rules.md — PASS (0 violations)

**Placement:** replaces §2.1–§2.10 and §2.12, inserts new §2.0; explicitly cedes §2.11 to ux.md. Collision-free (see aggregate check below); every existing §2.x number is preserved so no cross-reference breaks.

**Verified:**
- §2.3 terrain and §2.4 unit tables are value-for-value identical to the GDD (all seven terrain rows including Bridge −10% and Factory +15%; all four unit rows including Artillery 2–3 range and costs 100/300/200/150).
- §2.7 numbers verbatim: +100 factory / +25 town income, spawn-else-adjacent-else-wait, ~half-cost kills with the Tank +150 example, flag +500, capture N=1–2, 200 starting Fame, +25% repair (floored, min 1, capped) with the anti-fortress clause.
- The restructured §2.8 is logically equivalent to the master: the mutual-passivity guard subsumes the "applies only when both sides actually fought" precondition on key 2 (a nonzero tie at key 1 implies both fought by construction); towns still count in key 2 while domination stays factories-only; the tier table's "or territorial domination" restates §2.8's "ranked a **Decisive win**, equal to a flag kill"; the tally note that +500 can never appear in a capped tally is a derivation (a flag kill ends the match), not a rule change.
- Every number it moves is filed, not smuggled: the 20-turn cap pin (prose marks it "see change request pinning the value"), the per-turn-decay strike, exactly-half kill awards (50/75/100/150 — all four costs even, Tank 150 already the GDD's own example), the §2.10 "5 terrains → 6 + Factory tile" reconciliation (real internal GDD drift: §2.3 has carried 6 movement terrains + Factory since the Bridge/Factory fold while §2.10 and §1 still say "five"), the §1 scope-line edit correctly routed to the Director, and the Pillar 4 → Pillar 3 miscitation fix.
- New §2.0 PX-1..6 each cite a real rule source and a checkable instrument; T-CAP-01..08 are proposals handed to tech-director, not claims of existing tests. No unverified-claim.
- kb drift is declared, not silently worsened: missing Bridge/Factory rows, "only Town is capturable," missing territorial-domination trigger, missing Repair, "per land unit" vs "per movement class" — all flagged for merge-checklist step 3. No kb-desync.

## sections/ux.md — PASS (0 violations)

**Prior violations — both corrected:**
1. *Production-menu mock (was `contradiction`, §2.7).* The mock now reads `Fame: 250` with `Tank 300 ---- (need 50)` and the prose states "the mock's 250-Fame pool legally greys only the 300-cost Tank (`need 50`)". Legal under the §2.4/§2.7 cost table; shortfall arithmetic exact. **Fixed.**
2. *Scoreboard chevron (was `contradiction`, §2.8).* Both mocks now attach the chevron to the enemy's 600 (`Destr. 450   600◀` / `Destroyed  450      600 ◀`), and the bullet states "in the mock above the enemy leads at criterion 1, 600 combat Fame to 450 (§2.8: higher wins), so the chevron sits on the enemy column." The layout now teaches the rule the right way around. **Fixed.**

**Verified:**
- Placement (replace §2.11 wholesale) is precise; rules.md explicitly leaves §2.11 to this draft. Every element of the current §2.11 stub is retained; the art bullet survives as §2.11.7.
- The forecast worked example resolves correctly under the §3 formula: max(1, round(10 × 1.0 × 1.0 × 0.8) − 5) = 3, Tank 20 → 17, counter 0 by the range invariant (defender range 1 vs attacker at 2–3).
- All quoted stats match the GDD: Easy +150 / Hard −100, 200 starting Fame, costs 100/150/200/300, kill +150 on a Tank, flag +500 with "Decisive victory," income +100/+25, Bridge −10%, repair adjacency block, "AI moves instantly" (§2.8) with paced playback declared presentation-only.
- The Destroyed row's definition ("kills + undamaged-strike and flag bonuses, passive income excluded") mirrors §2.8 criterion 1 verbatim; the `— no engagements —` state renders the mutual-passivity guard.
- The three numbers the HUD cannot ship without (turn cap, capture N, move-undo) are filed as change requests — re-filed from stage 1, still unresolved in the master — not written into prose as settled. The undo key is explicitly conditional ("otherwise unbound").
- Voice: all system one-shots are ≤ 30 words, present-tense field-manual register, no banned words; faction voice appears only on the result screen, and each sample matches its faction's cadence per `kb_setting.md`. No voice-drift.
- The scoreboard mock's illustrative `3/6` is explicitly superseded by "N supplied by the scenario (Handoffs)"; scenario.md supplies N = 8 for the shipped map — illustrative only, worth aligning at merge (noted below, not a violation).

## sections/scenario.md — PASS (0 violations)

**Placement:** new §2.13 after §2.12, before §3; absorbs its stage-1 replay-cliff draft as §2.13.4 in-draft (no external citation). Collision-free.

**Verified:**
- All three ASCII maps audited hex-by-hex against their coordinate keys and spec tables, and agree exactly: *Ferrum Crossing* 11×9 = 99 with distribution Plains 75 / Woods 8 / Mountains 2 / Water 4 / Bridge 2 / Town 4 / Factory 4 summing to 99, water confined to rows 0–5, bridges (5,1)/(5,4), all ten deployment hexes on Plains and both home-factory hexes free; *Longwater March* 13×9 = 117 with 6 factories, 4 towns, mirrored, no Water; *The Causeway* 9×9 = 81, column-4 fully Water except bridges (4,2)/(4,6), factories/towns/woods/mountains all at their stated coordinates.
- Every GDD-sourced number is quoted correctly: ~4 factories = home per side + 2+ neutral (§2.7 verbatim for the shipped map), income and cost arithmetic (550-Fame producible force; 100 → ~225–250 ramp; 6×100 late-game income on Longwater), Bridge −10%, Mountains cost 3 / +40%, Artillery 2–3 with no counter, Tank 5 / Infantry 3 / Recon 7 move, Easy +150 / Hard −100.
- Longwater's "0–6 spread" for objectives-held follows the GDD's own idiom — §2.7 itself describes the "objectives held" spread purely by factory count ("a meaningful 0–N spread") — and the draft's Ferrum handoff states N = 8 (4 factories + 4 towns) correctly per §2.8 criterion 2, so the criterion is not misapplied anywhere it is load-bearing.
- Every number with no source antecedent — the 5-unit starting force, map dimensions, town counts, Longwater's 6th factory, per-scenario cap values, the ~55% seat-balance threshold — is filed in the change-request table or Open questions, explicitly "not silently adopted." No invented-fact.
- The Recon/Water class ambiguity and cross-Water Artillery fire are escalated with the conservative assumption stated and routed to rules-designer; the anti-turtle load on *The Causeway*'s lockout premise is grounded correctly in §2.8's guard/criterion-1 stack.
- kb drift (missing Bridge/Factory rows, missing domination trigger) flagged in the Director handoff, and the unowned title/lineage item is correctly left to the Director. No kb-desync, no scope-breach.

## sections/tech.md — PASS (0 violations)

**Prior violations — both corrected:**
1. *False evidence citation (was `dead-reference`).* The draft no longer cites a stage-1 artifact anywhere: "no stage-1 draft of this file exists as a repo artifact, so rather than cite one, this draft carries every load-bearing definition — stubs, gate IDs, the canonical hex order, the scenario-file fields, the UI binding contract, and the Q1–Q10 rule-gap register — inside itself," and Grounding closes with "**No stage-1 artifact is cited anywhere in this draft.**" **Fixed.**
2. *Undefined §4.7 dependencies (was `dead-reference`).* §4.7 is now filed in full inside the draft — all eight stubs, the shared conventions block (canonical hex order, axial distance), Stub 7's scenario-file fields including `isFlag`, Stub 8's binding contract, and Q1–Q10. Every ID cited by §4.8–§4.10 (T-SCN-01..04, T-HEX-07, T-UI-01..04, the Q register) resolves within the draft, the master GDD, or the two crew spec files the GDD's own §3 names. The merged §4 is self-contained. **Fixed.**

**Verified:**
- Every schema constant matches §2.3/§2.4/§2.7: unit rows 10/20/8/12 HP, 3/5/3/7 Move, 4/8/10/5 Atk, 2/5/1/3 Def, Artillery-only RangeMin 2 / RangeMax 3, costs 100/300/200/150; terrain defense 0/20/40/0/10/−10/15, move costs 1/2/3/—/1/1/1 with Water impassable-to-land; income 100/25; repair points Town + Factory; capture Infantry-only; starting Fame 200/200 with the difficulty handicap correctly modeled as match setup, not a scenario field.
- Provenance is honest: the only "built and gate-verified" claims are the four rows the GDD's §3 ledger already certifies (commit `5ffa8d6`, T-COMBAT-01..10, T-REPAIR-01..07, 17/17), and the draft states plainly "**Nothing else in this draft exists as code.**" No unverified-claim.
- Every rule the GDD does not state is parameterized on a numbered open question (Q1–Q13) rather than invented — pass-through, capture-N edge cases, kill-award exactness, income timing, AI tie order, undo, zero-RNG, replay scope — and the nine change requests (cap pin, exact kill values, movement-class caption, two new ledger rows, ledger test-ID annotations, §4.1/§4.4 amendments) are properly filed against existing text.
- The T-TURN gates restate §2.8 faithfully (tiebreak order, mutual-passivity guard with no fall-through, categorical tiers, domination factories-only at start of turn); T-FAME-01's fameTotal/fameCombat split correctly implements the income-exclusion rule; the save-is-a-replay design is grounded in the document's determinism guarantees and the §4.4 wk-5 conflict is handled by change request, not by silently moving the milestone.

---

## Cross-section checks

- **Placements, in aggregate:** rules.md takes §2.0 (new) + §2.1–§2.10 + §2.12 and explicitly cedes §2.11; ux.md replaces §2.11 wholesale; scenario.md inserts new §2.13 after §2.12; tech.md appends §4.7–§4.10 with amendments to §4.1/§4.4 filed as change requests. No two drafts target the same GDD text; every placement is mechanically mergeable. No placement-collision.
- **Escalations are consistent, not divergent:** the turn-cap pin (rules, ux, scenario, tech), capture-N (all four), the undamaged-strike bonus (rules Q1 / tech Q6), Recon's movement class (rules Q3 / scenario Q3+CR / tech Q2), and move-undo (ux CR / tech Q11, which correctly notes no gate assumes it) are each escalated to the Director with compatible framing; no draft answers another's open question unilaterally.
- **Handoffs interlock:** scenario's schema handoff matches tech's Stub 7 field list (per-scenario `turnCap`, capture-N, `isFlag`, validator invariants); ux's binding needs are covered 1:1 by tech's Stub 8 snapshot/queries and §4.9 event list; rules' T-CAP block seeds tech's Stub 5. Coordinate conventions differ (scenario odd-r offset vs tech axial) — a merge-time reconciliation for the Director, not a rule conflict, since both are internal representations of the same §2.2 pointy-top grid.
- **Merge-time alignment notes (not violations):** ux's illustrative `3/6` objectives mock vs the shipped map's N = 8; scenario's odd-r vs tech's axial coordinates; rules' §2.3 keeps the "per movement class" caption while tech's CR offers add-the-table-or-drop-it — Director picks one at Q2 adjudication.
- **kb_rules.md drift** (missing Bridge and Factory terrain rows, "only Town is capturable," missing territorial-domination trigger, missing Repair rule, "per land unit" caption) is pre-existing GDD↔KB drift, independently and correctly declared by rules.md and scenario.md for merge-checklist step 3. No draft would silently make the KB wrong.

---

**Verdict.** Run `stage-2` is a **PASS**: all four sections carry zero violations. The two authors re-spawned after the previous run corrected exactly what was filed — ux.md's production-menu mock is now legal under the §2.7 cost table and its chevron marks the true criterion-1 leader; tech.md's §4 is now self-contained, with the full §4.7 stub plan, gate IDs, and Q1–Q10 register defined in-draft and no citation of any nonexistent artifact — and the unchanged rules.md and scenario.md re-audited clean. Before merge the Director must: adjudicate the shared open rulings (turn-cap pin, capture N, undamaged-strike bonus, Recon movement class, move-undo, the 5-unit starting force and other scenario numbers, Q1–Q13) since several drafts carry provisional values contingent on them; merge at the stated placements (§2.0–§2.10/§2.12 from rules, §2.11 from ux, §2.13 from scenario, §4.7–§4.10 from tech) and reconcile the two coordinate conventions and the scoreboard's N; rebuild the derived .pdf/.txt; and re-sync `kb_rules.md`, whose terrain and victory tables are stale against both the current GDD and these drafts. Title/lineage framing remains unowned (no narrative-designer in this kit) and stays open for the Director.
