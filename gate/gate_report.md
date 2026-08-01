# Continuity gate — run `post-merge-15`

**Audit target:** `source/gdd.md`, md5 `84d3ad109e429caf08bc590a47ba71c7`
(`source/MANIFEST.txt` present; `kb_rules.md` `0c1884f9e06619b35ae7608c824e8b93`,
`kb_setting.md` `b3e9e89daaef1cdeb333e3fb4368d1c0`).
**Scope:** full re-audit. Nothing carried forward from `post-merge-14`; every
figure below was re-derived from the §2.13 layout blocks under §2.3 costs, in
odd-r with the §4.7 axial metric, not read off the previous report.
**`sections/`:** 22 files — 3 superseded drafts, 19 sealed addenda. No new draft
this run (the Director edited the master directly), so no placement collision is
possible and no draft is gated.

**Verdict: PASS — 0 violations across 13 areas.**

---

## 1. The remediation, checked against its three claims

### Claim 1 — no normative closure claim survives anywhere

Confirmed, by search and by reading. The live convention states the open
question and nothing more:

> **Stub 7, T-SCN-11 PRINT CONVENTION:** "WHETHER THIS SHOULD HARDEN INTO A
> CLOSED LIST OF PERMITTED FORMS IS Q30, unruled and deliberately left so. An
> earlier revision attempted that codification and withdrew it"

Q30's Assumption column matches it ("**What is left open is whether this should
harden into a closed list of permitted forms.** An earlier revision wrote that
closure and it was withdrawn"). A sweep for the withdrawn vocabulary — *admits*,
*exactly two*, *closed list*, *permitted forms*, *typed slot*, *compliance
sweep*, *first print* — returns nothing normative anywhere in §4.7 except those
two deliberate pointers, and nothing at all in §2.13. The three surviving
occurrences of "admits" (§2.13.1 facts 1–2 on offset rectangles, §4.7 Stub 7's
"at most ONE non-`none` value is well-formed") are geometry, not print
convention. §2.11.1's "exactly two: *attack* or *wait*" is the per-unit action
vocabulary, unrelated.

### Claim 2 — Q30 now reads coherently end to end

The repaired clause is the one specified, past-tensed:

> **Q30, Question column:** "A withdrawn revision of the print convention (§4.7
> Stub 7) named **two** relations for an "against" and gave two printed forms —
> a bare pair for owning-against-opposing, a named ceiling for
> measured-against-budget — but there are **three** quantities in play, and when
> this row was filed the third had neither a printed form nor an exclusion."

Read as a row: the Question describes a withdrawn attempt, is consistently
past-tensed on the state at filing ("was never stated at a print site", "when
this row was filed"), and closes on the question as originally posed — third
printed form, or exclusion. The Assumption states what is settled (bare pair is
set-quantified per Q28; a hex-scoped cost prints with its hex and its label) and
leaves the closure open. The Blocks cell reads "**Nothing computable**", which
is accurate: T-SCN-11's inputs, formula, unit set, reported integers, refusal
conditions and all three fixtures are identical either way.

No cell contradicts the stub. The Question's past-tensed "named two relations"
is a claim about the withdrawn revision's *contents*, not about what the live
convention admits — which is exactly the distinction that failed at
`post-merge-14`. The two forms it names both still appear in live prose (the
bare pair at fixtures (a)–(c), the named ceiling at T-SCN-08 fixture (c)), and
the Assumption cell says so, so no reader is left thinking either form was
removed with the codification.

### Claim 3 — nothing else moved

Verified against the whole document, not asserted. No figure, fixture,
invariant, refusal condition, deployment, week number, `T-` ID or `Q` ID differs
from what the same text supports. The register is Q1–Q30 with **ten ruled**
(Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28); Q29 and Q30 carry readings
and block nothing computable; Q4/Q5/Q6/Q8/Q9 state no reading and block their
gates outright, exactly as the §4.7 preamble says. §3's ledger is unchanged —
four rows verified at `5ffa8d6` (Combat, Test suite, Repair, Type-effectiveness;
T-COMBAT-01..10 + T-REPAIR-01..07 = the cited 17/17) and eight `*pending*`.

---

## 2. What was re-derived, not accepted

**All eight *Ferrum Crossing* routes (§2.13.2), re-measured hex by hex from the
r0–r8 block under §2.3 costs, with axial distance as the floor.**

| Infantry | → North (6,2) | → South (5,7) |
|---|---|---|
| West (1,3) | **6** (axial distance 5, +1 forced) | **6** (geodesic 6) |
| West (1,5) | **7** (distance 6, +1) | **5** (geodesic 5) |
| East (9,3) | **5** (distance 4, +1 through the Woods ring) | **6** (geodesic 6) |
| East (9,1) | **5** (distance 4, +1) | **7** (geodesic 7) |

Every printed hex sequence is adjacent under odd-r and prices to the printed
integer. Both structural claims hold: every North route costs hex distance + 1
(the only non-Bridge land approaches to (6,2) are the Woods ring (6,1)(7,2)(6,3),
each cost 2, and the Bridge route is one hex longer), and every South route is a
plain geodesic at 1 MP per hex. Fixture (b)'s pre-fix (9,5) → (5,7) re-measures
at **5** — axial distance 5, five cost-1 hexes — so the tie and the refusal are
real and un-implementable-away. Fixture (a)'s pairs re-derive as **5 against 6**
in both seats (West's South 5 against East's set minimum 6 from (9,3); East's
North 5 against West's set minimum 6 from (1,3) over Bridge (5,1)), and the
mispriced-objective-hex failure mode does report **5 against 5**.

**The Bridge-free counterfactual.** From (1,5):
`(2,6)(3,6)(3,7)(4,7)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)` =
1+1+1+1+1+1+1+1+2+2+1 = **13**, splitting 5 (the guided South lane) + 8 (the
east-bank tail) exactly as printed. From (1,3) = **14**, both through the
Mountain at (6,6) and Mountain-free via (5,7) at 6 + 8. The minimiser flip
confirms: with the Bridges West's set minimum to North is 6 achieved by (1,3),
(1,5) alone 7; without them the set minimum is 13 achieved by (1,5), (1,3) alone
14. So **5 against 13**, margin **8 MP**, with **14** correctly retained as the
(1,3)-scoped figure. East's 6 MP route to South uses no Bridge and reaches
column 5 only at the objective on row 7, below the river's southern end at
(5,5) — so it stands under either reading, and the allowance binds one of the
map's two objectives.

**The other four lanes.** *The Causeway* owning **3** MP —
(1,2)→(1,1)T→(2,1)→(3,2), the three-hex route beating the two-hex Mountain route
at 4, which is T-SCN-08 fixture (a) intact — opposing **5** from (7,3) over the
north Bridge, and Bridge-free the opposing route does not exist (column 4 is
Water end to end but for (4,2)/(4,5)). *Longwater March* owning **4** MP (all
Plains, axial distance 4), opposing **8** from (1,4) (axial distance 8). So
**3 against 5** and **4 against 8** both stand, and Q21's slack/margin ladder
re-derives: Ferrum 1/1, Longwater 2/4, Causeway 3/2.

**Symmetry.** ρ(q, r) = (W − H/2 − q, H − 1 − r) evaluates to (9 − q, 7 − r) on
Longwater (13 × 8) and (5 − q, 7 − r) on the Causeway (9 × 8); every printed
ρ-pair checks — homes, neutrals, towns, woods, mountains, and the Causeway's six
Water hexes in three pairs. On 9 × 9 the constant is 4.5 and (1,1) images to
column 6.5, as printed. The reserved μ(q, r) = (q + r − (H−1)/2, H−1−r) is a
genuine isometry — it sends (dq, dr) to (dq+dr, −dr), permuting the three terms
of the axial metric — and converts back to (c, H−1−r) in offset for both row
parities, so §2.13.1 fact 1 and Q26 are geometrically sound.

**Censuses and counts.** *Ferrum Crossing* 99 hexes: Plains 75 · Woods 8 ·
Mountains 2 · Water 4 · Bridge 2 · Town 4 · Factory 4 — every glyph counted off
the block. *Longwater March* 104: 86/4/4/0/0/4/6 (82.7% Plains against Ferrum's
75.8%, printed as 83% and 76%). *The Causeway* 72: 52/4/2/6/2/2/4. N = 8 and
N = 10 both check as factories + towns, matching §2.11.4 and §2.13.5. The
550-Fame producible starting force checks (2×100 + 200 + 150).

**§4.6 arithmetic, every line re-computed.** $0.69 and $1.725 per task from the
rate lines; 210 × $0.69 = $144.90; 32 × $1.035 = $33.12; subtotal $178.02;
substitution alternative $200.10; runtime $0.00465/turn, 88k and ≈$0.09 per
match, 17.6M and ≈$19 at 200 matches, $37.2 and $55.8 on Sonnet at the two
rates; 90M all-in; the 1.5× line 315 × $0.69 + 47 × $1.035 = $265.995, and
$267 − $265.995 = $1.005 exactly as printed. No figure disagrees with its own
inputs.

**Schedule.** §4.4 and §4.11 still describe one schedule: wk 1 = rows 1–3,
wk 2 = `{Move, Attack}` plus the §4.10 format and headless replayer with
T-INT-01/04 and T-SAVE-04 closing, wk 3 = rows 4–6 closing T-INT-02/03/05 and
T-SAVE-01/02/03/05/06, wk 4 = T-SAVE-07, wk 5 = slot I/O only. Row 7's ten
written invariants, four of which price a path (T-SCN-04, 06, 08, 11), match
Stub 7's acceptance line and §4.11's critical-path paragraph.

**Onboarding.** The three-branch beat schedule re-derives under rules 1–2 in all
three columns, including the fast lane's turn-3 untagged rule-2 call and turn-4
tagged repeat; the fast lane's premise holds because only *The Causeway*'s 3 MP
lanes are reachable in one Infantry move (Ferrum 5 MP, Longwater 4 MP, Move 3),
and "no lane on either 8-row map carries 4 [MP of slack]" is true at 4 and 3 MP.
Q21's "no starting unit sits on any of the eight routes" re-checks: none of the
ten deployment hexes appears in any priced sequence, and (9,1) is the origin of
two routes and interior to none.

**Mocks and derived UI numbers.** Forecast card: round(10 × 1.0 × 1.0 × 0.8) − 5
= 3, counter 0 out of range. Production menu: 300 − 250 = need 50. Scoreboard:
chevron on the enemy at 600 vs 450 (higher wins at criterion 1), 4/8 and 3/8
against N = 8, turn 12/20. HUD `+175/turn` is consistent with four objectives
held (one factory + three towns). Kill toast +150 = half a Tank's 300.

**Knowledge base.** `kb_rules.md` still agrees with §2.3, §2.4, §2.7 and §2.8
field for field, including the per-scenario turn cap, the negative Bridge
defense, and the three `[unpinned]` markers that correspond to Q4, Q5 and Q6.
`kb_setting.md` still agrees with §2.11.4's five faction/system result lines —
present tense, field-manual register, ≤ 30 words, no banned vocabulary, faction
voice confined to the result screen. No `kb-desync`.

---

## 3. The two candidates from `post-merge-14`, re-examined

Both were re-read against the current text, not against the earlier ruling.

**(a) Asymmetry (ii)'s "an "against" in this stub is the TWO-SEAT inequality a
fixture recomputes" against T-SCN-08 fixture (c)'s "This is the only "against"
in this stub that is not owning-vs-opposing".** This is the candidate the Q30
edit could touch, and it does not become filable. The changed clause moved from
a live normative assertion ("the convention admits exactly two relations") to a
past-tensed description of a withdrawn revision, which removes a claim about the
live convention rather than adding one. What remains is a universal-sounding
gloss inside a rationale for *withholding* the word "against" from a within-seat
comparison, and a self-declared exception at the exception's own site — and both
cite the same governing rule, "THE RELATION IS NAMED AT THE SITE", under which a
bare "against" is the two-seat inequality and a named-relation "against" ("the
6 MP ceiling", "never as a bare integer") may be something else. They reconcile
without a rule, and no reported integer, refusal condition or fixture depends on
the reconciliation. Not filed.

**(b) §2.13.1's "No opposing Infantry can arrive for fewer MP. That is the whole
of the inequality … and it is the property the gate checks."** Untouched by this
revision, and re-judged on its merits. Read at maximum strictness the phrasing is
non-strict where T-SCN-11 is strict ("EQUALITY FAILS"), and the note's own
preceding sentence calls a 5-against-5 tie "a race under any reading". But the
rule itself is stated correctly, strictly, and with its citation ten lines above
in the same note item — "must cost **strictly more MP** than the owning seat's
lane (T-SCN-11, §4.7)" — and the bullet's subject is what the margin *buys*, not
the operator: its three sibling bullets are all about purchase (it does not buy a
turn; deployment carries the rest; the stretch maps do buy one). A Director
locating the rule finds the strict form; the gloss understates it without
asserting a competing rule, and no gate, fixture or integer follows the gloss.
It is imprecise, not wrong. Not filed — and recorded here so the judgment is on
the record rather than repeated silently each run.

---

## 4. Findings by area

| Area | Verdict | Violations |
|---|---|---|
| §1, §1.5, §1.6 | PASS | 0 |
| §2.0–§2.10 | PASS | 0 |
| §2.11 (UI/UX + onboarding, incl. the beat schedule) | PASS | 0 |
| §2.12–§2.13.1 | PASS | 0 |
| §2.13.2–§2.13.7 | PASS | 0 |
| §3 (ledger) | PASS | 0 |
| §4.1–§4.3, §4.5, §4.6, §4.8–§4.10 | PASS | 0 |
| §4.4 + §4.11 | PASS | 0 |
| §4.7 Stubs 1–8 | PASS | 0 |
| §4.7 open-question register Q1–Q30 | PASS | 0 |
| `source/kb_rules.md` | PASS | 0 |
| `source/kb_setting.md` | PASS | 0 |
| `sections/` (no new draft) | PASS | 0 |

**Known-open, carried as stated and not counted as violations:** Q1–Q6, Q8–Q19
unruled with their assumptions in force; Q4, Q5, Q6, Q8 and Q9 stating no reading
and blocking their gates outright; Q29 and Q30 blocking nothing computable; §3's
eight `*pending*` rows against a stock Unreal `Source/`; title/lineage framing
unowned, which needs a `narrative-designer` this kit does not have.

---

**Verdict.** `post-merge-15` is **PASS**. The one-clause repair is exactly the
fix `post-merge-14` specified and nothing beyond it: the closure claim is gone
from Q30's Question column, no replacement closure appears in the stub, the
Assumption cell or §2.13, and the row now reads as a withdrawn attempt, a settled
partial reading, and one open question a Director can rule on without first
resolving a self-contradiction. Full re-derivation moved nothing — all eight
*Ferrum Crossing* routes, fixture (b)'s tie, both stretch maps' pairs, the 13/14
counterfactual split with its minimiser flip, three terrain censuses, both ρ-pair
lists, the Q1–Q30 register at ten ruled, §4.4/§4.11 as one schedule, §4.6's
arithmetic, and §3's ledger all re-derive to the printed figures, and both
knowledge-base files still parse true against §2. Nothing must happen before
merge: this document is clear to merge as it stands, and the next re-sync should
carry it forward unchanged.
