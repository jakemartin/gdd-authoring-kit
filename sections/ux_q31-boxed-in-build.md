# UX, UI & onboarding — q31-boxed-in-build draft (ux-onboarding-designer)

This addendum closes **no gate** and mints **no acceptance ID**. It is a
GDD-text-only correction to §2.11.5's production-menu spec, made to match the
Director's ruling on Q31: the Build buttons must stay enabled while a factory
is boxed in, and a click there still queues the build and commits its Fame,
exactly like any other build. No code is in scope — the ruling states the
backend (`Economy.h::queueBuild`, and the distinct `spawnBlocked`/
`buildWaiting` snapshot fields) already supports this with no changes needed.

I do not touch §2.7's rules prose or the §4.7/§2.13 register entries for Q31 —
those are owned by other authors this round and are (per the task brief)
already assigned to pick up the matching change on their side.

## Placement

§2.11.5 (Production menu & match-flow surfaces) — the production-menu mockup
and its footer/button-state description.

## Draft

### Pair 1 — §2.11.5, production menu bullet: footer swap and button state on a boxed-in factory

**OLD**

```
The spawn rule (§2.7: factory hex if free, else an adjacent free hex) is one static line in the footer. If the factory is fully boxed in, the footer swaps to `Boxed in — build waits for a free hex.` and Build buttons disable: the space-throttle (§2.7) explains itself at the moment it applies. Both the swap and the disable read the snapshot's per-factory `spawnBlocked` — board geometry, computed by the module, no board scan the widget runs for itself. They do not read `buildWaiting`, which is the narrower §2.7 fact that a build is holding this factory's slot until it spawns: a boxed-in factory need not have anything queued.
```

**NEW:**

```
The spawn rule (§2.7: factory hex if free, else an adjacent free hex) is one static line in the footer. If the factory is fully boxed in, the footer swaps to `Boxed in — build waits for a free hex.` but the Build buttons **stay enabled and clickable**: a click still queues the build and commits its Fame at that instant, exactly as it does at an open factory (§2.7's waiting-build rule; Q31, §4.7 — ruled: the player may queue into a boxed-in factory). The footer names the wait; it does not gate the click, and the commitment it is naming is visible before that click the same way any other build's cost is — the row already shows the price, and pressing `[Build]` spends it whether or not a hex is free the instant it does. The footer swap reads the snapshot's per-factory `spawnBlocked` — board geometry, computed by the module, no board scan the widget runs for itself. It does not read `buildWaiting`, which is the narrower §2.7 fact that a build is holding this factory's slot until it spawns: a boxed-in factory need not have anything queued, and the footer's wait line shows either way.
```

Ruling Q31 removes the one thing standing between the player and the AI-only
waiting-build path: the disabled button. The button's enabled state is now
the same regardless of `spawnBlocked`; only the footer text changes, and it
changes to *inform*, not to *block*. The Fame-committed-at-queue-time fact
(Q8(c), unchanged) is restated here because it is the fact a player must be
able to see before clicking — that is what makes an always-live button safe
to teach rather than a trap.

## Check results — sites swept, no pair needed (outside §2.11 ownership)

Swept `source/gdd.md` for every spelling of *boxed-in / boxed in*, *Boxed in*,
*disable*, *spawnBlocked*, *buildWaiting*, and *Q31*.

| Site | Text | Why no pair here |
|---|---|---|
| §2.7 (Economy & capture), "The player cannot currently reach the waiting case" | "§2.11.5 disables the Build buttons while a factory is boxed in, so for the player queue time and spawn time are the same instant, and the waiting build is an AI-only path today" | This is §2.7's rules prose, owned by `rules-designer` this round, not §2.11 material. It now describes a stale fact (it was true of the old §2.11.5 spec) but the brief for this task explicitly assigns any matching §2.7 change to that author, not to me. |
| §4.7 Spec Stub 8, per-factory block note | "the difference is the case §2.11.5 must display: a boxed-in factory with nothing queued has `spawnBlocked` true and `buildWaiting` false... Q31 asks whether a player may queue into a boxed-in factory; `buildWaiting` is the field such a ruling would bind to, and nothing here rules it" | §4.7 Spec Stub 8 text, owned by `tech-director`. It describes the two fields and notes the ruling was pending; it asserts nothing about button state itself, so it isn't falsified by this addendum, but the "nothing here rules it" clause is now stale and is that author's to update. |
| §2.11.8 Build ranking, must-have list | "production menu with grey/shortfall/boxed states" | Generic naming of visual states (grey/shortfall/boxed), not a claim about button enablement. Still accurate: a boxed-in factory still has a distinct visual state (the footer line), it's just no longer a *disabled* one. No pair needed. |
| §4.7 provenance ledger preamble | "Q31" listed among open-but-readable rows | §4.7/§2.13 register, owned by other authors this round per the task brief — not touched. |
| §4.7 provenance-chain paragraph, "the reachability seam the Q8(c) commitment ruling exposed against §2.11.5's Build-button rule (Q31)" | as quoted | Same register, same reason — not touched. |

## Change requests

None. This addendum implements the Director's ruling as given; it does not
propose any further rule or number change.

## Open questions for the Director

None raised by this addendum. (The stale §2.7 and §4.7 cross-references noted
above are flagged for their respective owners, not raised as open questions
here.)

## Handoffs

- `rules-designer` (§2.7): the sentence "§2.11.5 disables the Build buttons
  while a factory is boxed in... the waiting build is an AI-only path today"
  needs a matching update now that §2.11.5 no longer disables the buttons —
  the player-queued path now exists.
- `tech-director` (§4.7 Spec Stub 8): the schema note's closing clause,
  "nothing here rules it... today the waiting build is an AI-only path (Q31)
  and no gate asserts a player-queued one," is stale in the same way and is
  that author's call on how (or whether) to restate it, and whether a new
  gate should assert a player-queued `buildWaiting` case.

## Grounding

- Q31 ruling (Director, this round): Build buttons stay active while a
  factory is boxed in; the commitment (Fame spent at queue time,
  non-refundable) must be visible before the click, same as any other build.
- §2.7's waiting-build rule (unchanged, existing in `source/gdd.md`): a build
  spawns on the factory hex if free, else an adjacent free hex; if boxed in,
  the build waits and holds the factory's slot until it spawns; Fame is
  committed at queue time, not at spawn time, and is non-refundable (Q8(c),
  §4.7 — already ruled, not reopened here).
- §2.11.5's existing production-menu mockup (`source/gdd.md`, the `[Build]`
  rows with visible per-unit cost) as the surface that already shows the
  commitment before the click, for every build, boxed-in or not.
- Snapshot fields `spawnBlocked` and `buildWaiting` (`source/gdd.md` §4.7
  Spec Stub 8), cited by the ruling as already distinct and requiring no
  backend change — used here only to state which field the footer reads,
  unchanged from the prior text.
