> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-9 draft (tech-director)

## Placement

All six pairs land in **§4.7** (Pending-system gate plan): four inside the
**Stub 7** fenced block, two in the **open-questions register** row **Q22**.
No other section is touched. No map, lane number, terrain figure, week number,
`T-` ID or `Q` ID moves.

## Draft

### What the sweep found

I checked **every site in §4.7 that prints a measured pair**, plus the two
sites outside it that print one and are mine (§4.11 row 7's prose). The result
is not two independent slips — it is one convention that the stub uses
correctly nine times, states only *once* and only *late*, and gets backwards
at two sites. Full inventory:

| Line (source md5 `b75e2421…`) | Site | Pair type | Order | Verdict |
|---|---|---|---|---|
| 1801 | T-SCN-08 fixture (a), *The Causeway* | "3 **and** 3" | two seats' own lanes | correct — not an owning/opposing pair |
| 1808 | T-SCN-08 fixture (b), *Longwater March* | "4 **and** 4" | two seats' own lanes | correct — not an owning/opposing pair |
| 1811 | T-SCN-08 fixture (c) | "7 **against** 6" | measured vs **ceiling** | numbers right; **connective ambiguous** → pair 5 |
| 1900 | T-SCN-11 asymmetry (ii), *The Causeway* | "5 against 3" | owning/opposing | **INVERTED** → pair 2 |
| 1919 | T-SCN-11 asymmetry (iii), *Ferrum Crossing* | "5 against 6" | owning/opposing | correct |
| 1930 | T-SCN-11 "Reported like T-SCN-08" | "5 against 5" | owning/opposing | correct; **this is the only statement of the convention** |
| 1935 | T-SCN-11 fixture (a), *Ferrum Crossing* | "5 against 6 each way" | owning/opposing | correct, and expanded seat-by-seat |
| 1942 | T-SCN-11 fixture (a), asymmetric-pricing bug | "5 against 5" | owning/opposing | correct (tie; order-neutral) |
| 1947 | T-SCN-11 fixture (b), pre-fix deployment | "5 against 5" | owning/opposing | correct (tie; order-neutral) |
| 1955 | T-SCN-11 fixture (b) under the refused Q28 reading | "5 against 6" | owning/opposing | correct |
| 1958 | T-SCN-11 fixture (c), *The Causeway* | "3 against 5" | owning/opposing | correct — this is the site pair 2 is corrected *to* |
| 2070 (Q21) | "5/5, 4/4, 3/3" | two seats' own lanes (T-SCN-06) | — | correct; all three pairs equal, so no order to get wrong |
| 2071 (Q22) | all three maps | owning/opposing | **ALL THREE INVERTED** → pair 3 |
| 2071 (Q22) | "in 5 MP against West's own 5" | owning/opposing | tie, both seats named → pair 6, **optional** |
| 2071 (Q22) | "*Ferrum Crossing* reports **5 against 6**" | owning/opposing | correct — so Q22 currently contradicts itself, 300 words apart |
| 2077 (Q28) | "5 against 6", "pre-fix 5 against 5" | owning/opposing | correct |
| 2340 (§4.11) | "tied 5 against 5" | owning/opposing | correct (tie; order-neutral) |

**Is the convention stated ambiguously anywhere? Yes — in two ways, and both
are why this recurred.**

1. **It is stated once, at line 1930, and used at line 1900 first.** The only
   declaration of owning-then-opposing sits in T-SCN-11's *Reported* paragraph,
   thirty lines *after* asymmetry (ii) already prints a pair. A convention first
   used and later declared is a convention an editor can violate without ever
   reading it. Pair 4 moves the declaration to the point of definition — the
   line directly under the `min … > owning` formula, which is the first place
   the stub distinguishes the two sides at all.
2. **The connective "X against Y" carries two different relations inside one
   stub.** In T-SCN-11 it is owning-vs-opposing, where the passing form prints
   the **smaller** number first. In T-SCN-08 fixture (c) it is
   measured-vs-ceiling, where the **failing** form prints the larger number
   first ("7 against 6"). Those two habits point opposite ways, and (c) sits
   ninety lines above the sites that got inverted. Pair 5 names both sides of
   (c) explicitly rather than leaving order to carry the meaning. The stub's
   *other* distinction already works and is worth keeping deliberately: pairs
   joined by **"and"** (T-SCN-08 (a)/(b): "3 and 3") are the two **seats'** own
   lanes and assert no inequality; pairs joined by **"against"** are
   owning-vs-opposing. Pair 4 states that too.

**Nothing about the failing-fixture story changes.** Fixture (b) still fails,
still reports 5 against 5, and is still the pre-fix deployment. The corrected
Q22 row still records five lanes clearing and the sixth tying.

---

### The pairs

**Pair 1 — Stub 7, T-SCN-10: reserved-by-decision, not blocked-pending-answer.**
Q26 is ruled (§4.7 register, and the ruling text in the `symmetry` field says
so twice). "Blocked on Q26" says a ruling is outstanding when it has already
happened, and it contradicts the Acceptance line ~120 lines below, which reads
"T-SCN-10 is reserved and UNWRITTEN on Q26, which is a different state: nothing
is asserted, so nothing is waiting." The new text makes the reserved/blocked
distinction explicit and points at T-MOVE-07 — genuinely blocked, on the
genuinely unruled Q2 — as the contrast, so the two reserved-looking parentheticals
in this section can no longer be read as the same state. T-SCN-10 stays reserved
and unwritten; no gate is added.

**OLD**

```
   permutation: it sends (dq, dr) to (dq+dr, -dr), which permutes the three
   terms of the axial metric and leaves the distance unchanged. Blocked on Q26;
   no gate is written until the schema admits the value.)
```

**NEW**

```
   permutation: it sends (dq, dr) to (dq+dr, -dr), which permutes the three
   terms of the axial metric and leaves the distance unchanged. RESERVED BY
   DECISION, not blocked on an answer: Q26 is RULED — the enum stays at
   rot180 | none, so a horizontal mirror is undeclarable and there is nothing
   for a gate to verify. Nothing is waiting. It stays reserved rather than
   deleted because admitting the value later is purely additive — one enum
   value, this mu, and this invariant — and nothing passing today would then
   fail. Contrast T-MOVE-07 above, which IS blocked, on the unruled Q2.)
```

---

**Pair 2 — Stub 7, T-SCN-11 asymmetry (ii): *The Causeway*'s pair is printed
backwards.** Under the stub's owning-then-opposing order, "5 against 3" states
the owning lane as *longer* than the opposing route — a T-SCN-11 failure — in a
sentence whose entire point is that permitting Bridges on the opposing route
costs the map nothing. *The Causeway*'s lanes are 3 MP owning against 5 MP
opposing (§2.13.1 note 3; T-SCN-11 fixture (c), line 1958). One token moves;
the argument, the Bridge ruling and the vacuity reasoning are untouched.

**OLD**

```
                    STRICTER reading and it is the one asserted. Measured, it
                    costs nothing: The Causeway passes 5 against 3 in both
                    seats with the crossing permitted, and no other map in
                    the set has a Bridge on any opposing route.
```

**NEW**

```
                    STRICTER reading and it is the one asserted. Measured, it
                    costs nothing: The Causeway passes 3 against 5 in both
                    seats with the crossing permitted, and no other map in
                    the set has a Bridge on any opposing route.
```

---

**Pair 3 — register row Q22: all three maps inverted.** Same defect as pair 2,
at the register site, and here it reads as though *every* map in the set fails
T-SCN-11 — in the sentence that says five of six lanes cleared. The row already
prints *Ferrum Crossing* correctly ("reports **5 against 6 in both seats**")
about 300 words later, so as it stands the row contradicts itself. Corrected
pairs per §2.13.1 note 3 and §2.13.2's eight-route table: *Longwater* 4/8,
*Causeway* 3/5, *Ferrum* East lane 5/6. The new text also names the order at
the site, so the register no longer depends on a convention stated only inside
a fenced block it does not sit in.

**OLD**

```
Five of the six lanes cleared as drawn: *Longwater March* 8 against 4 in both seats, *The Causeway* 5 against 3 in both seats, *Ferrum Crossing*'s East lane 6 against 5.
```

**NEW**

```
Five of the six lanes cleared as drawn, each printed **owning against opposing** as T-SCN-11 reports it: *Longwater March* 4 against 8 in both seats, *The Causeway* 3 against 5 in both seats, *Ferrum Crossing*'s East lane 5 against 6.
```

---

**Pair 4 — Stub 7, T-SCN-11: state the print order at the point of definition.**
This is the fix for the *cause* rather than the two instances. The convention is
currently declared only in the *Reported* paragraph, after two sites have already
used it. Moving the declaration directly under the inequality it belongs to puts
it where anyone editing a measured pair is already reading, and states the
passing shape explicitly — smaller number first — so an inversion is visible
without cross-referencing another map. It also pins the "and" vs "against"
split that T-SCN-08's fixtures already observe. No number, invariant or ID
changes; four lines of contract text are added.

**OLD**

```
                min over the opposing seat's Infantry of cost(hex, objective)
                  >  the owning lane's cost
            This is the gate for §2.13.1's "uncontested, not merely
```

**NEW**

```
                min over the opposing seat's Infantry of cost(hex, objective)
                  >  the owning lane's cost
            PRINT ORDER, stated here at the definition and used at every
            site below: a measured pair reads OWNING FIRST, THEN OPPOSING.
            "a against b" passes exactly when a < b, so on a PASSING map the
            SMALLER integer comes first. Two integers joined by "and"
            instead (T-SCN-08's fixtures, "3 and 3") are the two SEATS' own
            lanes — a different pair, asserting no inequality.
            This is the gate for §2.13.1's "uncontested, not merely
```

---

**Pair 5 — Stub 7, T-SCN-08 fixture (c): disambiguate the one "against" that
is not owning-vs-opposing.** The numbers here are right and stay right. The
problem is that this is a *measured-vs-budget* comparison whose failing form
prints the larger integer first, sitting ninety lines above the owning/opposing
sites whose passing form prints the smaller integer first — the same connective
pointing two ways, which is what pairs 2 and 3 are instances of. Naming both
sides removes the reliance on order entirely.

**OLD**

```
              (c) A scenario whose lanes both cost 7 FAILS the T-SCN-06
                  ceiling, and the refusal reason CARRIES BOTH MEASURED
                  INTEGERS: an author needs to read 7 against 6, not merely
                  "too far" (Determinism, "refuses with a reason").
```

**NEW**

```
              (c) A scenario whose lanes both cost 7 FAILS the T-SCN-06
                  ceiling, and the refusal reason CARRIES BOTH MEASURED
                  INTEGERS: an author needs to read the measured 7 against
                  the 6 MP CEILING, not merely "too far" (Determinism,
                  "refuses with a reason"). This is the only "against" in
                  this stub that is not owning-vs-opposing: it compares a
                  measurement to a budget, and it is the one relation whose
                  FAILING form prints the larger integer first, so it names
                  both sides rather than relying on the print order.
```

---

**Pair 6 — register row Q22, the tie sentence. CONSISTENCY ONLY, SAFE TO SKIP.**
This site prints opposing-then-owning ("in 5 MP against West's own 5"), but
both integers are 5 and both seats are named in the sentence, so it states no
inequality and cannot be read backwards. It is listed because the sweep was
asked to confirm *every* site, and this is the last one that does not follow the
order pairs 3–4 establish. The rewrite moves no number and makes no new claim;
it only puts the owning lane first so the row reads in one direction throughout.
**If the Director prefers the narrative order — the tie is discovered from
East's side, which is how it was actually found — drop this pair and nothing
downstream changes.**

**OLD**

```
East's second Infantry at (9,5) reached West's South objective (5,7) in 5 MP against West's own 5.
```

**NEW**

```
West's South lane cost 5, and East's second Infantry at (9,5) reached that same objective (5,7) in 5 MP flat — 5 against 5, an exact tie.
```

## Build order

Unchanged by this revision. No week number, dependency or acceptance set moves;
row 7 still straddles the critical path and closes on row 3, and its acceptance
set is still `T-SCN-01..09, 11 (10 reserved-unwritten on Q26)` — wording §4.11
line 2323 already has right, and which pair 1 brings Stub 7 into line with.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3** for the priced half (T-SCN-04, 06, 08, 11) | Yes | T-SCN-01..09, 11 — **unchanged**; T-SCN-10 reserved-unwritten by the Q26 ruling |

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, T-SCN-10 | "Blocked on Q26; no gate is written until the schema admits the value." | Pair 1 | Q26 is ruled; "blocked" claims a pending answer and contradicts the Acceptance line below |
| §4.7 Stub 7, T-SCN-11 (ii) | "The Causeway passes 5 against 3" | Pair 2 | Inverted — prints a passing map as a failing comparison; contradicts fixture (c) |
| §4.7 register, Q22 | "*Longwater March* 8 against 4 …, *The Causeway* 5 against 3 …, *Ferrum Crossing*'s East lane 6 against 5" | Pair 3 | All three inverted against §2.13.1 note 3; row also contradicts its own later "5 against 6" |
| §4.7 Stub 7, T-SCN-11 | Print order stated only in the *Reported* paragraph, after two uses | Pair 4 | Root cause: the convention is declared later than it is used |
| §4.7 Stub 7, T-SCN-08 (c) | "read 7 against 6" | Pair 5 | Same connective, opposite relation; the one site whose failing form prints larger-first |
| §4.7 register, Q22 | "in 5 MP against West's own 5" | Pair 6 (**optional**) | Last site not in owning-first order; tie, so no claim is at stake |

## Open questions for the Director

**None new. No ID is filed.** The register stays **Q1–Q29, ten ruled** (Q7, Q20,
Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28).

Every finding this run was a transcription or status-word defect against rules
that already exist — §2.13.1 note 3 supplies all three map pairs, Q26 supplies
T-SCN-10's status, and the print order was already stated (once, late) at line
1930. Pair 4 promotes that existing statement to the point of definition and
pair 5 disambiguates a connective; neither invents a rule, so neither is a gap.
The one judgement call I am flagging rather than filing: **pair 6 is a style
choice, not a correctness fix** — see its note.

## Handoffs

- **`scenario-designer`** — no action. §2.13.1 note 3 (line 779) and §2.13.2's
  eight-route table (lines 938–950) are the authority I corrected §4.7 *to*;
  both already print owning-then-opposing and neither moves. If the print-order
  sentence added by pair 4 should also be echoed in §2.13.1's note, that is
  their section and their call, not mine.
- **`rules-designer`** — no action. No rule, cost, or comparison changes.
- **`ux-onboarding-designer`** — no action. The guided-opening directive strip
  and §2.11.6's beats are untouched; nothing here reaches a widget.
- **Director** — pair 6 needs a yes/no; the other five are corrections.

## Grounding

| Claim | Backed by |
|---|---|
| *The Causeway* is 3 MP owning against 5 MP opposing | §2.13.1 note 3, line 780 ("*The Causeway* **3 against 5**"); §4.7 T-SCN-11 fixture (c), line 1958 |
| *Longwater March* is 4 against 8 | §2.13.1 note 3, line 780 |
| *Ferrum Crossing* is 5 against 6 in both seats | §2.13.1 note 3, line 779; §2.13.2's eight-route table and its conclusion, lines 938–948; §4.7 Q28 row, line 2077 |
| Q26 is ruled and T-SCN-10 stays unwritten | §4.7 register Q26, line 2075; §4.7 Stub 7 `symmetry` field, lines 1700–1702; Stub 7 Acceptance, lines 1975–1976; §4.11 row 7 acceptance cell, line 2323 |
| T-MOVE-07 is genuinely blocked (the contrast pair 1 draws) | §4.7 Stub 3, lines 1538–1539; register Q2, line 2051 — Q2 carries no ruling |
| The print order is owning-then-opposing | §4.7 T-SCN-11 *Reported*, line 1930 ("carries BOTH measured integers, owning and opposing"); the inequality itself, lines 1861–1862 |
| T-SCN-08 (a)/(b) print two seats' lanes, not an owning/opposing pair | §4.7 lines 1801–1808; cross-checks against Q21's "5/5, 4/4, 3/3", line 2070 |
| Q22 currently contradicts itself | Line 2071 contains both "East lane 6 against 5" and "reports **5 against 6 in both seats**" |
| Fixture (b) still fails at 5 against 5 and is the pre-fix deployment | §4.7 T-SCN-11 fixture (b), lines 1944–1957; §4.11 line 2340 |
| Source is current | `source/MANIFEST.txt`: `gdd.md … md5=b75e2421d92f492f7fd6634c7617d00b` |
