# Researching Research

## Conditions for Autonomous Mathematical Work

This is a living research atlas about how mathematical work can remain useful after the context window, session, or individual agent that produced it is gone.

The central question is:

> What must exist around an agent for long-horizon mathematical work to become cumulative, inspectable, and replaceable?

The projects collected here are experiments around that question. Some build formal tools. Some represent unfinished work. Some build persistent research worlds or coordination infrastructure. oncewhere is a creative work that asks a neighbouring question: what should remain available after an immediate human experience has passed?

This repository is a map of a research trajectory, not a monorepo and not a list of finished products. Each project keeps its own identity and evidence. The map is allowed to change as the evidence changes.

## How to read this repository

1. Start with [the research arc](research-arc.md).
2. Read [the current questions](current-questions.md).
3. Open a project card for the question, evidence, my role, and limits of the result.
4. Use fixed commit links when you need to audit a historical claim.
5. Read [the evidence and status contract](docs/evidence-and-status.md) before comparing projects.

## Research map

| Theme | Question | Representative work |
| --- | --- | --- |
| Reliable action and feedback | Can an agent make a mathematical move and receive a trustworthy local signal? | [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md), [Pi Lean Tools](projects/pi-lean-tools.md) |
| Unfinished mathematical work | How should active attempts, valid certificates, and unresolved obligations coexist? | [Metron](projects/metron.md) |
| Persistent research worlds | Can research state survive replacement of agents and sessions without turning provisional material into truth? | [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md), [MathWeave](projects/mathweave.md) |
| Organization and replaceability | What does a research organization control, and what does replacement actually mean? | [PMW Research Platform](projects/pmw-research-platform.md), [Aperture](projects/aperture.md), [Rights in the Exponent](projects/rights-in-the-exponent.md) |
| Evidence and diagnosis | How can we explain a swarm's outcome without collapsing evidence into a single score? | [Agent Math Frontier](projects/agent-math-frontier.md), [Trace analysis](projects/trace-analysis.md) |
| Adjacent creative work | What does it mean to preserve a shared experience as something that can be revisited? | [oncewhere](projects/oncewhere.md) |

## Selected work

<!-- project-index:start -->
| Project | Theme | Status | Visibility | Evidence |
| --- | --- | --- | --- | --- |
| [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) | reliable-action-and-feedback | experimentally-observed | private | branch experiment/e13; fixed commit to be pinned after branch audit |
| [Pi Lean Tools](projects/pi-lean-tools.md) | reliable-action-and-feedback | prototype | private | branch codex/frontier-probe-command; fixed commit to be pinned after branch audit |
| [Metron](projects/metron.md) | unfinished-mathematical-work | prototype | private | branch metron/f0-runtime-v2; fixed commit to be pinned after branch audit |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md) | persistent-research-worlds | experimentally-observed | private | https://github.com/yuan-chengzhi/persistent-mathematical-worlds/commit/4880f184c60bd34181302c5343ec0db95f154851 |
| [MathWeave](projects/mathweave.md) | persistent-research-worlds | implemented | private | https://github.com/yuan-chengzhi/MathWeave/commit/393fca141df3aa990378edb53fa3cc9e89445011 |
| [PMW Research Platform](projects/pmw-research-platform.md) | organization-and-replaceability | prototype | private | https://github.com/yuan-chengzhi/pmw-research-platform/commit/d28748c8a8a67d19b17ccbd347b8c5a853c33782 |
| [Rights in the Exponent](projects/rights-in-the-exponent.md) | organization-and-replaceability | analysis | private | https://github.com/yuan-chengzhi/rights-in-the-exponent/commit/2b7291c564d609a68d580f5279af4c3c8ee27136 |
| [Aperture](projects/aperture.md) | organization-and-replaceability | experimentally-observed | private | https://github.com/yuan-chengzhi/aperture-worlds/commit/5e72b0b1859bee3ae71babbecf6eadd20c9061bc |
| [Agent Math Frontier](projects/agent-math-frontier.md) | evidence-and-diagnosis | implemented | public | https://github.com/yuan-chengzhi/agent-math-frontier/commit/e5fb06928f26e0762e62c17b2cea241c29c40918 |
| [oncewhere](projects/oncewhere.md) | adjacent-creative-work | adjacent-work | private | https://github.com/yuan-chengzhi/oncewhere/commit/9ea4c02316cdd96ca5c4f8f6d7a0af2bdcfe240 |
| [Trace analysis](projects/trace-analysis.md) | evidence-and-diagnosis | research-thread | internal | analysis thread; repository link will be added if the apparatus becomes a standalone project |
<!-- project-index:end -->

## My role in the work

The cards distinguish the existence of a repository from my contribution to it. My work across the mathematical-agent projects has included prompt and experiment design, proof-state optimisation, trace analysis, issue fixing, data analysis, figures, proofreading, and revisions.

## How this atlas evolves

Adding a repository should be a small, reviewable change:

1. Create a stable card in projects/<id>.md.
2. Add one entry to project-index.json.
3. Pin the strongest evidence to a commit or tag when possible.
4. Write what the evidence establishes and what it does not establish.
5. Run python scripts/build_index.py --write to refresh the mechanical table.
6. Update current-questions.md only when the new project changes the live questions.
7. Add a decision record only when the interpretation of the research arc changes.

The script and workflow are deliberately small. They check structure and maintain the index; they do not generate research meaning, personal contributions, or stronger claims than the evidence supports.

## What this repository does not claim

- It does not present a single finished autonomous mathematical research system.
- It does not treat implementation as proof of scientific effectiveness.
- It does not use one universal progress score for every kind of unfinished work.
- It does not claim that shared state is the same thing as shared cognition.
- It does not place oncewhere inside the mathematical-agent system; its connection is thematic and personal.

[中文说明](README.zh-CN.md)
