# Technical design — compiler naming and the unmet week-1 goal (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All four replacement pairs were applied verbatim to the master GDD and merged
> on 2026-08-02. Re-applying them would fail (the OLD anchors no longer match)
> or, worse, **double-apply pair 4**, which is an insertion: its NEW text keeps
> the anchor sentence and appends to it, so that anchor survives by design.
> Gate record: run `compiler-gap-2`, PASS, zero violations, after one blocking
> run. Master GDD md5 `97ccf0e9cc8c3f72adfaca10bd42d862` →
> `83fb9acbc19b8c6cb7adb037ea50d150`. Later changes to these sections need a NEW
> addendum file.
>
> Four replacement pairs: three in §4.7/§4.9 for the
> compiler-detection wording (Ruling 1), one in §3 for the unmet week-1
> "Playable via debug commands" goal (Ruling 3). Each **OLD** block was grepped
> against `source/gdd.md` (md5 `97ccf0e9cc8c3f72adfaca10bd42d862`) and returns
> **exactly one** match. No NEW block contains a fenced block, so every pair
> below uses three backticks.
>
> **Ruling 2, recorded so it is not re-opened:** §4.4 is a plan and records no
> outcomes. No pair here touches it; status lives in §3's ledger, §3's status
> paragraph and §4.11.
>
> **Not in scope, per Fact B:** §3's populated-rows paragraph says the Combat
> suite was certified "on a live `g++`/`clang++` compile+run" at `5ffa8d6`, and
> that the week-1 run was "under clang++ and MSVC both". Both stay true and
> neither is edited.

---

## Pair 1 — §4.7 head, the gate that compiles the stubs

Documentation-only: the gate detected one compiler at both commits Fact A
checks, `5ffa8d6` and `c224825`, so the old text understated it rather than
describing a tooling change.

**OLD**
```
engine dependencies, compiled by the same `g++`/`clang++` + `python run.py` gate
that certified Combat (§3 ledger). Where a stub needs a rule the GDD does not
```
**NEW**
```
engine dependencies, compiled by the same `python run.py` gate that certified
Combat (§3 ledger). That gate detects **one** compiler per run — the first of
`g++`, `clang++`, `c++` or `cl` found on PATH — so a green run is green under
whichever one it found, not under all four. Where a stub needs a rule the GDD
does not
```

## Pair 2 — §4.9 §1, where the certified sources are compiled

Same understatement, one section over.

**OLD**
```
sources live canonically in the crew repo, and each §4.7 stub joins them as it
lands — where the `g++`/`clang++` + `python run.py` gate
runs (§3 ledger). The UE project vendors them verbatim into a UBT runtime
```
**NEW**
```
sources live canonically in the crew repo, and each §4.7 stub joins them as it
lands — where the `python run.py` gate runs (§3 ledger), under the single
compiler that gate detects: the first of `g++`, `clang++`, `c++` or `cl` found
on PATH. The UE project vendors them verbatim into a UBT runtime
```

## Pair 3 — §4.9, T-INT-04

T-INT-04 is an acceptance ID, so its text states the *any-one* semantics
outright: a bare list of four compilers would read as requiring all four, which
is neither the ruling nor what `crew/tools.py` implements. The block sits inside
a fenced spec stub that uses no backticks, so the NEW text uses none either.

**OLD**
```
  T-INT-04  no engine deps: StratRules compiles standalone under the existing
            g++/clang++ gate — the gate run itself is the assert
```
**NEW**
```
  T-INT-04  no engine deps: StratRules compiles standalone under the existing
            python run.py gate, using whichever single compiler that gate
            detects — the first of g++, clang++, c++, cl found on PATH. Any
            one of them compiling clean satisfies this invariant; it does not
            require all four. The gate run itself is the assert
```

## Pair 4 — §3, the status paragraph: the unmet week-1 goal

§4.4's week-1 cell claims two things; only the ledger rows are recorded. The
second claim is recorded here, negatively, at the sentence that already narrates
what week 1 did not close. The OLD fragment is mid-line — §3's status paragraph
is one long source line — and is reproduced byte-exact.

**OLD**
```
What week 1 did **not** close is everything after it: rows 4–8 hold no code,
```
**NEW**
```
What week 1 did **not** close is everything after it: rows 4–8 hold no code, and §4.4's week-1 goal "Playable via debug commands" is **unmet** — at `c224825` five tracked sources define `main()` (`cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/selfplay.cpp`), which are four test harnesses and a combat duel simulator, and none of them drives a unit around a board,
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §4.7 | Head paragraph, the sentence naming the compile gate |
| 2 | §4.9 | Item 1, *Module layout — one source, two compilers* |
| 3 | §4.9 | The integration spec stub, invariant T-INT-04 |
| 4 | §3 | The italic *Status: live tracker* line, mid-sentence |

No pair touches §1, §2, §4.4, §4.5, §4.8, §4.11 or the Q register. Pairs 2 and 3
are both in §4.9 and do not overlap: pair 2 is prose above the stub, pair 3 is
inside it. §4.9 item 1's heading "one source, two compilers" is unaffected — it
contrasts the standalone gate with the UBT build, not two gate compilers.

## Grounding

Fact A backs pairs 1–3: `crew/tools.py::find_compiler()` returns the first of
`g++`, `clang++`, `c++`, `cl` on PATH, byte-identical at `5ffa8d6` and
`c224825`. Fact B is why §3's two existing compiler sentences are left alone.
Fact C backs pair 4, at its stated extent — sources defining `main()` in the
tracked tree at `c224825`. The three OLD anchor sites and their uniqueness come
from `source/gdd.md`; `Playable via debug commands` occurs once in the document,
and `selfplay`, `duel simulator` and `entry point` occur zero times, so no other
site restates the claim pair 4 corrects.

## Open questions for the Director

None. Both rulings closed the questions that produced them.

## Change requests

None.

## Handoffs

None owed. No pair states, restates or implies a rule, a map fact, or a screen
layout.
