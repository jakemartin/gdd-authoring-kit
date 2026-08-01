> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> The Q30 substring swap it supplies in Open questions **was also applied**.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-13 draft (tech-director)

## Placement

Four pairs. **Three in §4.7, Stub 7** — two inside T-SCN-11's `PRINT CONVENTION`
(its opening count sentence, and the hex-scoped-quantity paragraph), one inside
T-SCN-11 asymmetry (ii)'s *Ferrum Crossing* bullet (the minimiser-flip sentence).
**One in the §4.7 open-questions register**, in Q30's row, on the "two relations"
claim only.

Plus one **corrigendum**, recorded here and nowhere else, against a figure in
`sections/tech_post-merge-12.md`. That file is sealed and applied; it is not
edited.

No map hex, no lane cost, no terrain figure, no week number, no `T-` ID and no
`Q` ID moves. T-SCN-10 stays reserved and unwritten. The register stays
**Q1–Q30**, still **ten ruled** (Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27,
Q28); Q30 stays **unruled with a conservative reading in force**. Nothing in
`sections/` is edited; this file is the whole delta.

---

## Draft

### Corrigendum to `sections/tech_post-merge-12.md` — plainly labelled, not an edit

**The wrong figure.** `post-merge-12`'s minimality table priced **(1,3) → (5,8)
at 6, total 15**. The map yields **7, total 16**. The Director's own measurement
and the gate's agree with each other and against mine: the approach vector from
**(1,3)** is **5 / 6 / 7** to (5,6) / (5,7) / (5,8), not 5 / 6 / 6.

The same wrong 6 appears three times in that sealed file, and all three are
wrong in the same way:

| Where in `tech_post-merge-12.md` | Printed | Correct |
|---|---|---|
| Minimality table, row `(5,8)`, "From (1,3)" and "Total" | 6, total **15** | **7**, total **16** |
| Re-read table, row "14 is d(1,3), unchanged": `(1,3) approaches at 5/6/6 → min(5+9, 6+8, 6+9)` | 5/6/**6**; third term **6+9** | 5/6/**7**; third term **7+9** |
| Handoff to `continuity-gate`: "the approaches (5/5/5 and 5/6/**6**)" | 5/6/**6** | 5/6/**7** |

**What did not move, and why nothing has to.** d(1,3) is the minimum over the
three crossings. Correcting the third term *raises* it:

    before (wrong):  min(5+9, 6+8, 6+9) = min(14, 14, 15) = 14
    after  (right):  min(5+9, 6+8, 7+9) = min(14, 14, 16) = 14

The binding term was never the (5,8) route. **d(1,3) = 14 stands, via the (5,7)
route at 6 + 8**, exactly as the document prints it. d(1,5) = 13 is untouched —
its approach vector 5 / 5 / 5 and the tails 9 / 8 / 9 are unchanged and were
re-derived independently by the gate. The set minimum is still **13**, the
margin still **8 MP**, the 5 + 8 split still holds, the Mountain-free 14 still
holds, East's 6 is still unchanged.

**Nothing propagated.** The GDD never printed a (5,8) approach or a total of 15;
those figures existed only in `post-merge-12`'s working. Every integer that
reached §4.7 — 6, 7, 13, 14, 5, 8 — is correct as printed. This corrigendum
therefore changes no pair, past or present.

**What it does change is my confidence in one habit.** The three wrong prints
were one measurement copied forward twice without re-derivation. The two figures
I *did* re-derive per print — the (5,7) tail of 8 and the (1,5) approach of 5 —
are the two that survived. The lesson is narrow and I am applying it below: a
figure is checked at each print, not once at its source.

---

### Violation 1 — the convention broken by its own example

**What is actually wrong.** `post-merge-12`'s Pair 3 wrote a rule and
`post-merge-12`'s Pair 1 broke it in the sentence Pair 3 then cites as its
worked case:

| The rule | The breach |
|---|---|
| "A HEX-SCOPED COST IS A THIRD QUANTITY WITH NO BARE FORM. Print it with its hex and the words *from (c,r) alone, not the set minimum*, or do not print it in an 'against' at all." | "with Bridges permitted West's cheapest is **(1,3) at 6 against (1,5) at 7**; without them it is **(1,5) at 13 against (1,3) at 14**" — four hex-scoped costs, inside two "against"s, in neither permitted form. |
| "Two relations in this stub print an 'against'" | The stub then prints **three**: owning-vs-opposing, measured-vs-budget, and this within-seat ranking. |

**Why it happened, which matters for the fix.** The rule was written by reading
the *defect* (a hex figure in the opposing slot) and generalising to "label the
hex figure." It was never tested against the *repair* sitting eleven lines
above it. Had it been, the first thing it would have hit is the point below,
which is also the reason I am choosing as I am.

#### The choice, on the merits

Q30 poses two: **give the third quantity a printed form**, or **bar it from an
"against"** and rewrite the sentence without one. I am taking the **bar**, and
the argument is not aesthetic.

**1. The mandated label is false on the case that most needs it.** The
minimiser-flip sentence prints four costs of West's own Infantry. Two of them —
(1,3)'s 6 with Bridges, (1,5)'s 13 without — **are their reading's set
minimum**. The required words "not the set minimum" cannot be written beside
them without asserting something false. So a third form cannot be a single
form: it would need a minimum branch and a non-minimum branch, and the minimum
branch is not a hex-scoped print at all — it is the set figure naming the hex
that achieves it, which the convention *already* permits and which is what
fixture (a) does. A "third form" therefore decomposes, on inspection, into one
existing form plus one label. There is no third form to give.

**2. "Against" is the invariant's comparison operator, and every instance of it
is gate-recomputed.** T-SCN-11's "against" is a checked inequality *between the
two seats*; T-SCN-06's is a measurement against a ceiling. Both are recomputed
by a fixture. Ranking one seat's own units against each other asserts nothing
any gate could ever check — it is arithmetic about the *input* to a comparison,
not a comparison. Putting it in the same word is precisely the ambiguity the
convention exists to kill, and the convention's own governing line ("THE
RELATION IS NAMED AT THE SITE, and integer order identifies nothing") gets
harder to satisfy with every relation admitted.

**3. The count stops being a count.** Under the third-form route the sentence
becomes "three relations", which the next new quantity makes four — a
descriptive tally in normative text, which is the same defect class as the one
under repair. Under the bar it becomes **a closed, typed list of two**, true by
rule rather than by census. That is the difference between fixing this instance
and removing the failure mode.

**What the bar does not cost.** It does not delete the 14, which was the
objection `post-merge-12` raised against the stricter option — and that
objection was aimed at a *stricter* alternative than the one I am taking.
Forbidding the quantity **outright** would delete the 14. Forbidding it **in an
"against" slot** does not: the 14 survives twice in the bullet, once as the
labelled `FROM (1,3) ALONE` print and once in the rewritten flip sentence. The
flip survives whole — and states its insight more directly, because "the set
minimum is 13, achieved by (1,5)" names the relation that actually changes (the
*achiever*), where "at 13 against 14" only implied it.

#### The one thing the bar must not break

The **owning** term of a bare pair is itself a cost from a named hex — fixture
(a) prints "West's South lane 5 **from (1,5)** against East's cheapest 6 **from
(9,3)**", and both of those name hexes. A bar worded as "no hex-scoped cost in
an 'against'" would make fixture (a) illegal and would have been a fifth
self-inflicted defect. So the bar is worded on the **slots**, not on the
presence of a hex:

- **left slot** = the owning lane (T-SCN-06's *named* hex — hex-scoped by
  definition and legal) or the measurement under budget;
- **right slot** = the opposing **set minimum**, or the named ceiling;
- a cost from **some other** named hex is the third quantity and fits neither
  slot.

That wording keeps fixture (a), fixture (b)'s "5 against 5" from (9,5), the WHY
paragraph's "5 against 13", the Causeway's "3 against 5" and T-SCN-08's "7
against the 6 MP ceiling" all legal and untouched. It bars exactly one thing:
the within-seat ranking.

---

### The pairs

**Pair 1 — Stub 7, T-SCN-11 `PRINT CONVENTION`, the opening count sentence.
REQUIRED (Violation 1, first half).** Turns a census into a rule. No relation,
form, order rule or integer changes; the two bullets that follow are untouched
and are not part of the OLD block. Anchor `Two relations in this stub` occurs
once in the master.

**OLD**

```
            integer order identifies nothing. Two relations in this stub
            print an "against":
```

**NEW**

```
            integer order identifies nothing. EXACTLY TWO relations may
            print an "against". The list is CLOSED and the SLOTS ARE
            TYPED — that is a rule, not a count of what happens to
            appear below:
```

---

Pair 2 replaces the whole hex-scoped paragraph including its Q30 pointer. Three
things are new in it and each is there because the old text lacked it: the
**typed slots** (without which the bar would outlaw fixture (a)'s own owning
term), the **first-print** clause (without which the bullet's later reference to
its own labelled 14 would be non-compliant), and the **sentence-versus-slot**
clause (without which the WHY paragraph's "NOT the 14 measured from (1,3) alone"
would be non-compliant). All three are cases the old rule got wrong, found by
running the new rule over the text it governs before writing it down. No integer
in this pair is new: 5, 6, 13, 14, (1,3), (1,5) are all already in the stub.

**Pair 2 — Stub 7, T-SCN-11 `PRINT CONVENTION`, the hex-scoped-quantity
paragraph. REQUIRED (Violation 1, second half).** Anchor
`A HEX-SCOPED COST IS A THIRD QUANTITY` occurs once in the master.

**OLD**

```
            A HEX-SCOPED COST IS A THIRD QUANTITY WITH NO BARE FORM.
            Print it with its hex and the words "from (c,r) alone, not
            the set minimum," or do not print it in an "against" at all.
            Naming the hex beside a bare pair is safe ONLY when that hex
            IS the minimiser, which is what fixture (a) does. The danger
            is concrete, not stylistic: the minimising unit can CHANGE
            under a counterfactual, so a figure taken from the shipped
            minimiser stops being the minimum — asymmetry (ii)'s Ferrum
            Crossing bullet is exactly that case, where excluding the
            Bridges moves West's minimiser from (1,3) to (1,5) and the
            figure from 14 to 13.
            WHETHER THE THIRD FORM IS A PRINTED FORM OR A PROHIBITION IS
            Q30, unruled. The reading in force is the one written here,
            and it binds prose only: no invariant, fixture, reported
            integer or refusal condition depends on it.
```

**NEW**

```
            THE SLOTS, so that "typed" is checkable and not a mood. The
            LEFT slot is the owning lane — T-SCN-06's NAMED hex, which
            is why "5 from (1,5)" is a legal left term (fixture (a)) —
            or the measurement being budgeted. The RIGHT slot is the
            opposing SET MINIMUM, or the named ceiling. Nothing else
            may stand in either slot.
            A HEX-SCOPED COST IS A THIRD QUANTITY: a cost measured from
            some OTHER named hex, neither the owning lane nor a set
            minimum. IT IS BARRED FROM THE "AGAINST" FORM ENTIRELY, not
            merely from the bare pair. It is printed OUTSIDE an
            "against", in one of exactly two ways.
              - IT IS NOT THE MINIMUM: name its hex and say so — "14
                from (1,3) alone, not the set minimum." The label is
                required at that figure's FIRST print in a passage; a
                later reference back to the same labelled figure need
                not repeat it.
              - IT IS THE MINIMUM: then it is not a hex-scoped print at
                all. It is the SET figure, and it may name the hex that
                ACHIEVES it — "13, achieved by (1,5)" — which is what
                fixture (a) does and why fixture (a) is safe.
            THE BAR IS ON THE SLOT, NOT ON THE SENTENCE. A hex-scoped
            figure may appear in a sentence that carries an "against",
            provided it is named as what the "against" is NOT —
            asymmetry (ii)'s WHY paragraph does exactly this, printing
            "5 against 13 ... and NOT the 14 measured from (1,3)
            alone."
            WHY A BAR AND NOT A THIRD PRINTED FORM. Two reasons, the
            first decisive. (1) THE LABEL WOULD BE FALSE ON THE CASE
            THAT MOST NEEDS IT. Asymmetry (ii)'s minimiser-flip
            comparison prints four costs of West's own units, and TWO of
            them ARE their reading's set minimum, so "not the set
            minimum" could not truthfully be written beside them. A
            third form would therefore have to split into a minimum
            branch and a non-minimum branch — and the minimum branch is
            not a hex-scoped print at all, it is the set figure naming
            its achiever, which is already legal above. There is no
            third form left to give. (2) AN "AGAINST" IN THIS STUB IS A
            CHECKED INEQUALITY BETWEEN THE TWO SEATS, and every instance
            is recomputed by a fixture. Ranking ONE seat's own units
            against each other asserts nothing any gate could check, so
            it does not belong in the same word; and admitting it would
            make the count above three, which the next new quantity
            would make four. A closed typed list removes the failure
            mode where a third form would only increment it.
            The danger guarded is concrete, not stylistic: the
            minimising unit can CHANGE under a counterfactual, so a
            figure taken from the shipped minimiser stops being the
            minimum — asymmetry (ii)'s Ferrum Crossing bullet is exactly
            that case, where excluding the Bridges moves West's
            minimiser from (1,3) to (1,5).
            WHETHER THE BAR STANDS, OR THE CONVENTION INSTEAD GAINS A
            THIRD PRINTED FORM, IS Q30, unruled. The reading in force is
            the one written here, and it binds prose only: no invariant,
            fixture, reported integer or refusal condition depends on it.
```

---

Pair 3 is the sentence Violation 1 names, rewritten to obey Pair 2 without
losing anything. Every figure is one already in the bullet — 6, 7, 13, 14, 5, 8
— and the two set minima are now printed *as* set minima with their achievers,
which is what makes the flip legible: the changing thing is the **achiever**,
and the old wording only implied it.

**Pair 3 — Stub 7, T-SCN-11 asymmetry (ii), the *Ferrum Crossing* bullet's
minimiser-flip sentence. REQUIRED (Violation 1, the worked example).** Anchor
`EXCLUDING THE BRIDGES MOVES THE MINIMISER` occurs once in the master. The rest
of the bullet — the `FROM (1,3) ALONE` print, the `MINIMISED OVER WEST'S
INFANTRY` print, both route strings, and the entire East half — is not in the
OLD block and does not move.

**OLD**

```
                      EXCLUDING THE BRIDGES MOVES THE MINIMISER, which
                      is the whole reason the two figures differ: with
                      Bridges permitted West's cheapest is (1,3) at 6
                      against (1,5) at 7 (§2.13.2); without them it is
                      (1,5) at 13 against (1,3) at 14. The 1 MP is the
                      APPROACH, not the Mountain — (1,5) reaches (5,7)
                      in 5 and (1,3) in 6, while the tail from (5,7)
                      costs 8 for both, and (1,3) has a Mountain-free 14
                      as well. So a figure measured from the SHIPPED
                      minimiser is NOT the counterfactual minimum, and
                      that is the trap this bullet exists to name.
```

**NEW**

```
                      EXCLUDING THE BRIDGES MOVES THE MINIMISER, which
                      is the whole reason the two figures differ. WITH
                      the Bridges, West's set minimum to North is 6,
                      achieved by (1,3); (1,5) alone costs 7, not the
                      set minimum (§2.13.2). WITHOUT them, the set
                      minimum is 13, achieved by (1,5); (1,3) alone
                      costs 14, not the set minimum. THE ACHIEVING UNIT
                      IS NOT THE SAME UNIT under the two readings — that
                      is the flip, and it is why this bullet's two
                      figures are two DIFFERENT quantities rather than
                      one quantity corrected. No "against" is printed in
                      this comparison, deliberately: these are four
                      costs of ONE seat's own units, while an "against"
                      in this stub is the TWO-SEAT inequality a fixture
                      recomputes (PRINT CONVENTION; Q30).
                      The 1 MP is the APPROACH, not the Mountain —
                      (1,5) reaches (5,7) in 5 and (1,3) in 6, while the
                      tail from (5,7) costs 8 for both, and (1,3)'s 14
                      is achievable Mountain-free as well. So a figure
                      measured from the SHIPPED minimiser is NOT the
                      counterfactual minimum, and that is the trap this
                      bullet exists to name.
```

---

Pair 4 touches Q30's row at the "two relations" claim and nowhere else, per the
brief. One note on where that claim actually sits: it is in Q30's **Question**
column, as the sentence *"The print convention (§4.7 Stub 7) names two relations
and gives two printed forms — … — but there are three quantities in play, and
the third has no form."* The last column ("Assumption in force until ruled")
makes no two-relations claim, so this is the only copy in the row, and the
instruction that both copies need fixing is only executable against this one. If
the intent was the last column instead, drop this pair — the register would then
carry a count the stub no longer supports, which is the thing to weigh, but it
is the Director's call and not a figure.

**Pair 4 — §4.7 register, Q30, the "two relations" sentence. REQUIRED
(Violation 1, the second copy).** **Substring replacement**, unique in the
master (`names two relations and gives two printed forms` occurs once). No other
clause of Q30 is touched: the row stays **unruled**, its Blocks cell stays
`Nothing computable`, and its Assumption cell is not edited.

**OLD**

```
The print convention (§4.7 Stub 7) names two relations and gives two printed forms — a bare pair for owning-against-opposing, a named ceiling for measured-against-budget — but there are **three** quantities in play, and the third has no form.
```

**NEW**

```
The print convention (§4.7 Stub 7) admits **exactly two** relations into an "against" and gives two printed forms — a bare pair for owning-against-opposing, a named ceiling for measured-against-budget — but there are **three** quantities in play, and when this row was filed the third had neither a printed form nor an exclusion.
```

---

### Compliance sweep of the text I am writing, not the text I am replacing

This is the check the Director asked for, run in the direction that has failed
four rounds running: every "against" and every hex-scoped figure in my own
**NEW** blocks, tested against the rule those same NEW blocks state.

| My new text | Form used | Legal under Pair 2? |
|---|---|---|
| Pair 2: `"5 from (1,5)" is a legal left term` | Owning lane, quoted, no "against" | Yes — and it is the clause that *makes* fixture (a) legal |
| Pair 2: `"14 from (1,3) alone, not the set minimum."` | Hex-scoped, labelled, outside an "against" | Yes — the non-minimum branch, quoted as its own example |
| Pair 2: `"13, achieved by (1,5)"` | Set minimum naming its achiever | Yes — the minimum branch |
| Pair 2: quoting `"5 against 13 … and NOT the 14 measured from (1,3) alone."` | "against" with set-minimum right slot; 14 named as what it is not | Yes — by the slot-not-sentence clause, which exists for this |
| Pair 2: `moves West's minimiser from (1,3) to (1,5)` | Names hexes, prints no cost | Yes — no figure to scope |
| Pair 3: `West's set minimum to North is 6, achieved by (1,3)` | Minimum branch | Yes |
| Pair 3: `(1,5) alone costs 7, not the set minimum` | Non-minimum branch, first print of 7 in the passage, no "against" | Yes |
| Pair 3: `the set minimum is 13, achieved by (1,5)` | Minimum branch | Yes |
| Pair 3: `(1,3) alone costs 14, not the set minimum` | Non-minimum branch, labelled; also a repeat of the bullet's earlier labelled 14 | Yes on both counts |
| Pair 3: `(1,3)'s 14 is achievable Mountain-free as well` | Repeat reference to a figure labelled twice above | Yes — by the first-print clause, which exists for this |
| Pair 3: `(1,5) reaches (5,7) in 5 and (1,3) in 6`; `the tail from (5,7) costs 8 for both` | Route decomposition, no "against", no slot | Yes — the bar is on slots |
| Pair 3: `No "against" is printed in this comparison` | A claim about the sentence containing it | True — checked by reading the whole NEW block for the token; it appears only inside that quoted-negation phrase and in `an "against" in this stub is the TWO-SEAT inequality`, neither of which is a printed pair |
| Pair 1: `EXACTLY TWO relations may print an "against"` | The rule | True after Pairs 2 and 3 land: the within-seat ranking is gone, and the stub's remaining "against"s are owning-vs-opposing and measured-vs-budget only |

**And the sweep of the text I am not changing**, to confirm the bar breaks
nothing already shipped:

| Existing site | Slots | Verdict |
|---|---|---|
| Fixture (a) "5 from (1,5) against East's cheapest 6 from (9,3)" | Owning lane / set minimum naming its achiever | **Legal** — the reason the bar is worded on slots |
| Fixture (a) "East's North lane 5 from (9,3) against West's cheapest 6 from (1,3)" | Same | **Legal** |
| Fixture (a) "reports 5 against 5 and refuses" | Owning / opposing minimum under a mispriced implementation | **Legal** |
| Fixture (b) "must FAIL, reporting 5 against 5" from (9,5) | Owning / pre-fix set minimum | **Legal** |
| Fixture (b) "under the Q28 reading REFUSED, (b) passes at 5 against 6" | Explicitly the narrow reading, labelled | **Legal** |
| Fixture (c) *Causeway* "3 against 5 in both seats" | Owning / opposing minimum | **Legal** |
| T-SCN-08 fixture (c) "7 against the 6 MP ceiling" | Measurement / named ceiling | **Legal** |
| §2.13.2 "both report the same pair: 5 against 6" | Owning / opposing minimum | **Legal** |
| Asymmetry (iii) "passes in both seats at 5 against 6" | Same | **Legal** |
| Asymmetry (ii) WHY "5 against 13 … NOT the 14 measured from (1,3) alone" | Owning / set minimum; 14 outside both slots | **Legal** — slot-not-sentence |
| Asymmetry (ii) WHY "goes from 6 to 13 against an unchanged owning 5" | Set minima / owning lane | **Legal** |
| ORDER paragraph "prints '7 against 5' … and '5 against 5' on a tie" | Failing forms of the same two relations | **Legal** |
| Reported-like line "an author reads '5 against 5'" | Owning / opposing | **Legal** |

**One existing site is non-compliant and I did not touch it — see Open
questions.** Q30's Question column repeats the flip sentence verbatim,
"`(1,5) at 13 against (1,3) at 14`". The brief scopes that cell to the
two-relations sentence only, so it is out of scope for this file; the exact
replacement is in Open questions, ready to apply.

---

## Build order

Unchanged. No week number, dependency, acceptance set or `T-` ID moves. Row 7
restated for completeness only:

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3** for the priced half (T-SCN-04, 06, 08, 11) | Yes | T-SCN-01..09, 11 — **unchanged**; T-SCN-10 reserved-unwritten (Q26) |

Nothing here changes what any gate computes. T-SCN-11's inputs, formula, unit
set (Q28), reported integers, refusal conditions and all three fixtures are
identical before and after all four pairs, and every fixture reports the same
pair it reported before this file. The corrigendum changes no gate either: the
figure it corrects was never in the GDD and never in a fixture.

The standing risk is the one this round makes concrete rather than the one
`post-merge-12` named. **§4.7's prose is the one part of row 7 with no gate**,
and the failure that keeps recurring is not a wrong measurement — the
measurements have held — but a *rule stated in new prose that the same new prose
violates*. That is not gate-shaped: no invariant a build could run reads the
document's own conventions. The mitigation is procedural and I have made it
explicit above as the compliance sweep: **run the rule you just wrote over the
text you just wrote, including the sentence that cites it as an example.** All
three unstated clauses in Pair 2 — typed slots, first-print, slot-not-sentence —
were found that way, and each of them corresponds to a passage the previous
wording would have outlawed.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, `PRINT CONVENTION` opening | "Two relations in this stub print an 'against'" | **Pair 1** | A census in normative text, and already false — the stub prints three. Replaced by a closed, typed list of two, true by rule. |
| §4.7 Stub 7, `PRINT CONVENTION` hex-scoped paragraph | "Print it with its hex and the words … or do not print it in an 'against' at all" | **Pair 2** | The optional branch becomes the rule. Adds the three clauses the old wording lacked — typed slots (else fixture (a) is illegal), first-print (else the bullet's own repeat is illegal), slot-not-sentence (else the WHY paragraph is illegal). |
| §4.7 Stub 7, asymmetry (ii), flip sentence | "(1,3) at 6 against (1,5) at 7 … (1,5) at 13 against (1,3) at 14" | **Pair 3** | The breach itself. Rewritten with no "against": set minima with achievers, non-minimum members labelled. The flip is stated more directly, since the achiever is what changes. |
| §4.7 register, Q30, Question column | "names two relations and gives two printed forms … the third has no form" | **Pair 4** | The second copy of the count. Made normative and past-tensed on the gap, since the third quantity now has both a form and an exclusion. |
| **Not requested, listed for the record** | `sections/tech_post-merge-12.md` minimality table, `(1,3) → (5,8) = 6, total 15` | **None — corrigendum only** | The file is sealed and applied. Correct figures 7 / 16 are recorded above; d(1,3) = 14 and every downstream figure are unaffected. |

## Open questions for the Director

**No new IDs.** The register stays **Q1–Q30**, still **ten ruled**. Q30 stays
**unruled with a conservative reading in force** — the reading is now the *bar*
rather than the *third form*, which is a change of which conservative reading is
written in, not a ruling, and it remains free: it costs words and never a map, a
gate, an integer or a fixture.

**1. Q30's ruling is now a live choice between two things I have both written
down.** The bar is in force (Pairs 1–3) and the third form is the recorded
alternative. My argument for the bar is above; the counter-argument, stated
fairly, is that the bar makes one sentence longer and requires a reader to know
that "achieved by" and "against" are different relations. If you rule the third
form instead, Pair 3 reverts to something close to its current text and Pair 2's
`WHY A BAR` paragraph is deleted — a two-block follow-up, no integers.

**2. Q30's Question column still contains the non-compliant flip sentence, and
the brief put it out of scope.** It reads "with them permitted West's cheapest
is (1,3) at 6 against (1,5) at 7, without them it is (1,5) at 13 against (1,3)
at 14." Under the bar that is the exact print Pair 3 removes from the stub. If
you want it aligned, the substring swap is:

    OLD:  with them permitted West's cheapest is (1,3) at 6 against (1,5) at 7,
          without them it is (1,5) at 13 against (1,3) at 14.

    NEW:  with them permitted West's set minimum is 6, achieved by (1,3), and
          (1,5) alone costs 7; without them the set minimum is 13, achieved by
          (1,5), and (1,3) alone costs 14.

No integer moves. I have not applied it, because the brief scopes that cell to
the two-relations sentence. The case for leaving it: the register is a record of
what went wrong, and a row may reasonably quote the defect. The case against: it
does not read as a quotation, it reads as the explanation.

**3. Q30's Assumption column is now narrower than the reading in force, and I
did not edit it.** It states the labelling rule ("printed only with its hex and
the words …") and fixture (a)'s carve-out, both of which remain **true**; what it
does not state is the bar, the typed slots or the first-print clause. It is
incomplete rather than wrong, which is why I left it — but if you would rather
the register carry the whole reading, one sentence appended to that cell does
it. Note that its closing gloss, "forbid the third quantity outright, which
would **delete the 14**", describes a *stricter* option than the bar and is still
accurate as a description of that stricter option; the bar does not delete the
14.

**4. Nothing else is new.** No rule gap was found while writing these gates that
does not already have an ID. The one thing I would call a gap is not a rule
gap: the document has no gate for its own print conventions, and I am not
proposing one, because a convention that binds prose only is checked by reading
and by the sweep above, not by a build.

**Still unowned, unchanged:** title / lineage framing (`narrative-designer`,
Tier 2, not in this kit).

## Handoffs

- **`scenario-designer`** — **no action.** No cell of §2.13.2 moves. The
  standing note from `post-merge-12` is unchanged and still the thing to know
  before editing *Ferrum Crossing*: West's Bridge-free minimum to North is
  achieved by **(1,5)**, not (1,3), and it runs through (5,7), so an edit to the
  southern pass, to (7,6), or to West's second Infantry deployment changes a
  figure §4.7 prints and no gate recomputes. The corrigendum above touches only
  a working figure in a sealed addendum, not the map.
- **`rules-designer`** — **no action.** No rule, cost, comparison, operator or
  ruling changes. `>` stays the ruled comparison, equality still fails, Q21,
  Q22, Q26 and Q28 keep their rulings verbatim, and no ruled row is edited.
- **`ux-onboarding-designer`** — **no action.** §2.11.6's guided-opening beats
  and the directive strip are untouched.
- **`continuity-gate`** — **Pairs 1, 2 and 3 must land together**; Pair 3's
  compliance is defined by Pair 2, and Pair 1's count is only true once Pair 3
  lands. Pair 4 is independent and is a pure substring swap. **Two things to
  re-derive if you re-measure:** the corrigendum's `min(5+9, 6+8, 7+9) = 14`,
  and the claim that after Pair 3 the stub contains no "against" whose slots are
  anything but {owning lane | budgeted measurement} × {opposing set minimum |
  named ceiling} — the second sweep table above enumerates every site I checked,
  and the one I did **not** fix (Q30's Question column) is named there and in
  Open questions rather than omitted.
- **Director** — three of four pairs are one repair; Pair 4 is its second copy.
  Nothing waits on a ruling. Q30's two options are both written down: the bar is
  in force, the third form is recorded, and switching is a two-block follow-up
  with no integers in it.

## Grounding

| Claim | Backed by |
|---|---|
| The convention's opening sentence says "Two relations in this stub print an 'against'" | §4.7 Stub 7, `PRINT CONVENTION`, current master (`source/gdd.md`) |
| The stub then prints a third | §4.7 Stub 7 asymmetry (ii): "(1,3) at 6 against (1,5) at 7 … (1,5) at 13 against (1,3) at 14" — a within-seat ranking, neither of the two named relations |
| That print is in neither permitted form | §4.7 Stub 7 `PRINT CONVENTION`: hex-scoped costs must carry "from (c,r) alone, not the set minimum" or not appear in an "against"; the flip sentence does neither |
| The mandated label would be false on two of the four costs | (1,3) = 6 is West's minimum with Bridges (§2.13.2 route table: (1,3) 6, (1,5) 7); (1,5) = 13 is West's minimum without them (`post-merge-12` measurement, gate-confirmed: crossings (5,6)/(5,7)/(5,8), tails 9/8/9, (1,5) approaches 5/5/5) |
| The owning term of a bare pair is itself hex-scoped | §4.7 Stub 7 fixture (a): "West's South lane 5 from (1,5) against East's cheapest 6 from (9,3)"; T-SCN-06 quantifies on a NAMED hex (asymmetry (iii)) |
| Every "against" in the stub is fixture-recomputed | §4.7 Stub 7 fixtures (a)(b)(c) and T-SCN-08 fixture (c); the within-seat ranking appears in no fixture |
| The bar does not delete the 14 | It survives in the bullet's `FROM (1,3) ALONE` print and in Pair 3's "(1,3) alone costs 14, not the set minimum" |
| d(1,3) = 14 stands after the corrigendum | min(5+9, 6+8, 7+9) = min(14, 14, 16) = 14; the binding term is the (5,7) route at 6 + 8, which the corrigendum does not touch |
| The (5,8) approach from (1,3) is 7, not 6 | Director's measurement and the gate's, in agreement; `post-merge-12`'s 6 is the error being recorded |
| Set minimum 13, margin 8 MP, 5 + 8 split, Mountain-free 14, East's 6 all unaffected | All derive from (1,5)'s route and the (5,7) crossing; neither involves the (5,8) approach |
| Nothing propagated from the wrong figure | The GDD prints no (5,8) approach and no total of 15; the figure existed only in `post-merge-12`'s minimality table, re-read table and gate handoff |
| Q30's row: the "two relations" claim is in the Question column only | §4.7 register, Q30 — the Assumption column states the labelling rule and fixture (a)'s carve-out, and makes no count |
| Register extent and ruled count | §4.7 register: Q1–Q30, ruled Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 = ten; Q30 stays unruled |
| The register may hold an unruled row with a reading in force, and may change which reading | §4.7 register preamble: "where a reading is stated, it is the conservative one … chosen so that a later ruling loosens behavior rather than invalidating a passing gate"; the bar is free by the same test the third form was |
| All four anchors are unique in the master | `Two relations in this stub`, `A HEX-SCOPED COST IS A THIRD QUANTITY`, `EXCLUDING THE BRIDGES MOVES THE MINIMISER`, `names two relations and gives two printed forms` — one occurrence each |
| Source is current | `source/MANIFEST.txt`: `gdd.md <- …\Stratocracy_Prototype_GDD.md md5=f74039a1345d58b03052a58f840c7526`, the hash named in the brief |
