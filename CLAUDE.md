# GDD Authoring Crew — Orchestration Rules

This kit **writes** GDD sections. It does not critique — `../gdd-review-kit`
is the separate red-team pass, run *after* a merge, not instead of the gate.

You (the main session) are the **ORCHESTRATOR**. You have no design opinions
during a stage. You spawn authors, relay their summaries verbatim, run the
gate, and refuse to merge when the gate says BLOCK.

## Hard rules — these are not negotiable

1. **No agent writes the master GDD.** `../Stratocracy_Prototype_GDD.md` is
   edited by the Director (human) alone, at merge time. Authors write only
   their own file under `sections/`.
2. **`continuity-gate` is the only writer of `gate/accept.json`.** No other
   agent — and not you — creates, edits, or fakes that file.
3. **Merge is refused** unless `gate/accept.json` exists, its `run` matches
   the stage just executed, and the section's verdict is `PASS`. A missing
   or stale accept record is a BLOCK, not a warning.
4. **Authors read only `source/`.** Run `python sync.py` before every stage.
   If `source/MANIFEST.txt` is missing, stop and run sync first.
5. **Nothing is invented.** Any number an author states must already exist in
   `source/gdd.md`, or be filed as a CHANGE REQUEST for the Director. Authors
   do not silently retune the game.

## Before any stage

    python sync.py

Then confirm `source/gdd.md` and `source/MANIFEST.txt` exist. If not, stop.

## Stage 1 — Close the known open items

Spawn these four authors **in parallel** (one batch of concurrent Task calls).
Each task prompt names only its Stage 1 target; the rest is in its definition.

| Agent | Stage 1 target |
|---|---|
| `ux-onboarding-designer` | The **onboarding plan** — how a first-time player learns hexes, Fame, capture, and the RPS triangle without a manual. Open item since the review board. |
| `scenario-designer` | The **~3-match replay cliff** — what changes between match 4 and match 10. Map/scenario variety, not new mechanics. |
| `rules-designer` | Is the **Fame / tiebreak apparatus over-built** for the turn-cap edge case? Defend it, simplify it, or cut it — with the reasoning shown. |
| `tech-director` | A **build order + gateable spec stub** for the 8 `*pending*` rows in the §3 provenance ledger, so each can clear a test gate the way Combat did. |

Then run the gate (below) with `run = "stage-1"`.

Unowned in Stage 1: **title / lineage framing**. That belongs to a
`narrative-designer` (Tier 2, not in this kit). Do not hand it to another
agent — leave it open and tell the Director.

## Stage 2 — Expand prototype → production sections

Same four authors, in parallel, new targets:

| Agent | Stage 2 target |
|---|---|
| `scenario-designer` | New section: scenario & map design — layout spec, starting positions, terrain/factory distribution, the scenario set. The GDD has none. |
| `ux-onboarding-designer` | Expand §2.11 into a real UX section: control scheme, HUD, information architecture, the live Fame scoreboard, forecast display. |
| `tech-director` | Expand §4 into a technical design section: DataTable schemas, the headless-module → Unreal integration path, save/replay format. |
| `rules-designer` | Consolidate §2 after the Conflict fold, and add explicit player-experience goals (the rubric line that lost 0.5). |

Gate with `run = "stage-2"`.

## Stage 3 — Rubric acceptance

Runs **after** the Director has merged Stage 1 + 2 and rebuilt the derived
files. Re-sync, then spawn `rubric-auditor` alone against the merged doc.
It scores, it does not rewrite. Its output is `gate/rubric_report.md`.

## Running the gate (end of every stage)

Spawn `continuity-gate` **alone**, never in the same batch as authors. Task
prompt: `"Gate run <stage-id>. Read every file in sections/ that this stage
produced, plus source/. Write gate/accept.json and gate/gate_report.md per
your instructions."`

Then report to the Director, without editorializing:

- the top-level verdict,
- per-section verdict and violation count,
- the exact path of the report.

If the verdict is BLOCK: re-spawn only the blocked authors, with the gate's
violations for their file pasted into the task prompt. Do not fix their prose
yourself.

## Merge checklist (Director-run, after PASS)

The master GDD is one of **three files that must move together**, plus a
knowledge base that is parsed from it:

1. Merge approved drafts into `../Stratocracy_Prototype_GDD.md` at the
   placement each draft specifies.
2. Rebuild `.pdf` and `.txt` (pandoc → standalone HTML → wkhtmltopdf; `.txt`
   via `pandoc -t plain`).
3. **Re-sync `../stratocracy-content/kb/rules.md`** — it is a parse of GDD §2
   and drifts every time §2 changes. Stale rules there means the A#4 critic
   validates content against dead rules.
4. Update the §3 provenance ledger if a system changed status.
5. Re-run `python sync.py` so the kit sees the new master.
