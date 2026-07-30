# GDD Authoring Kit — Stratocracy

Four discipline agents **write** GDD sections; a fifth **gates** them against
the live document before anything is merged. An optional sixth scores the
merged result against the course rubric.

This is the authoring counterpart to `../gdd-review-kit`, which critiques but
writes nothing. Both are used: this kit produces sections, the review kit
red-teams the merged document afterward.

## Requirements

[Claude Code](https://code.claude.com/docs), installed and authenticated.
Python 3 for `sync.py`. No API key, no dependencies.

## The crew

| Agent | Discipline | Writes |
|---|---|---|
| `rules-designer` | Systems Designer | `sections/rules.md` |
| `scenario-designer` | Level / Mission Designer | `sections/scenario.md` |
| `ux-onboarding-designer` | UX/UI Designer | `sections/ux.md` |
| `tech-director` | Technical Director | `sections/tech.md` |
| `continuity-gate` | QA / Doc Control | `gate/accept.json`, `gate/gate_report.md` |
| `rubric-auditor` *(Tier 2, Stage 3)* | Producer / Assessment | `gate/rubric_report.md` |

**No agent is removable.** Authors produce drafts; the gate is the only writer
of the accept record; the merge step refuses without a PASS. Delete any one and
the chain stops — the same property that made the A#3 crew's roles defensible.

Deliberately **not** in this kit (Tier 2, add when Tier 1 lands):
`economy-designer`, `narrative-designer`, `producer-scope`, `art-audio-director`.
The course flags 5+ agent types for a solo dev as scope creep; six is already
the ceiling.

## Running it

    python sync.py          # pull the live GDD + KB into source/
    claude                  # start Claude Code in this directory

Then, one at a time:

    Run Stage 1.
    Run Stage 2.
    Run Stage 3.

Read the gate report between stages. Stage definitions and targets are in
`CLAUDE.md`.

**First run only:** `.claude/agents/` did not exist when you last started
Claude Code, so restart it once after cloning this kit — the directory watcher
only covers directories that existed at session start.

## What you get

    sections/rules.md        draft + change requests + open questions
    sections/scenario.md
    sections/ux.md
    sections/tech.md
    gate/accept.json         machine-readable verdict, per section
    gate/gate_report.md      violations with GDD line references
    gate/rubric_report.md    Stage 3 only

Every draft states its own **placement** (which GDD section number it goes
into, before or after what), so merging is mechanical rather than a judgment
call about where things live.

## Architecture

See `diagram.mmd`.
