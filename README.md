# Researching Research

**Chengzhi Yuan · Multi-agent systems · AI for Mathematics**  
[中文](README.zh-CN.md) · [Research development](research-development.md) · [Research graph](docs/research-graph.md) · [Current questions](current-questions.md)

I study the collective behavior, organization, and capability scaling of Agent Swarms. I enjoy building tools, architectures, and shared environments, anticipating how they might shape agents' actions, and testing those expectations in actual runs. Unexpected behavior often becomes the start of the next question. Formal mathematics, especially long-horizon proof work, is my main setting at present.

**How can many agents' local explorations become sustained collective progress? Can a system discover, implement, test, and retain effective improvements—and eventually improve how it searches for and evaluates changes?**

This is a living personal research map, not a finished unified system. It records artifacts and results alongside unfinished explorations, unsuccessful goals, and observations that changed my understanding.

> **Public entry points:** This research map is public. Visit [pi-lean-tools](https://github.com/yuan-chengzhi/pi-lean-tools) for Lean tools and [oncewhere](https://github.com/yuan-chengzhi/oncewhere) for the interactive creative project. Access checked on 2026-10-15.
>
> **Reading and access:** Project summaries remain readable here even when their original sources are private. The Putnam platform and reports remain private; their research description is retained without a public-code-release commitment. Other code, run data, and team manuscripts may also require permission. See [access and sharing](docs/access-and-sharing.md).

## Start with the work

| Work | My contribution | Output and status |
| --- | --- | --- |
| [Putnam 2025: proof loop and Lean tools](projects/putnam-2025.md) | Experiment platform, prompts, tooling, runtime diagnosis, and result analysis | All 12 problems reached internal `final_verified`; eight parallel attempts per problem; approximately 5.5 hours summed over reported problem runtimes. Pinned report, not an official contest score. |
| [ContextSwarm: FLT progress and system iteration](projects/contextswarm.md) | Checking local results against upper-level proof needs; diagnosing a missing parent-route query; prompt and reference-access improvements | Team system, ten-task FLTBench, and ICLR 2027 submission. Full FLT formalization remains unfinished. |
| [Collaboration analysis of the same FLT campaign](projects/flt-proof-weaving-aamas.md) | Reconstruction by proof object, version, and event-time state; cases, diagnostic notes, selected visualizations, and manuscript revisions | AAMAS 2027 submission; approximately 100B tokens and 40,000 aggregate agent-hours across the team campaign, not another independently built system. |

Two earlier or parallel explorations complement this work: [Collective Acceleration](projects/collective-acceleration.md) models progress sharing through stochastic processes and networks; [TacticWorld](projects/tacticworld.md) proposes learning structured consequences of alternative tactics from the same state. Its complete training and evaluation remain unfinished. These entries have different evidence and maturity levels.

## How practice changed the question

In the Putnam A5 comparison, agents without an added natural-language-first prompt still chose to reason before writing Lean. This made me distinguish **providing working capabilities** from **prescribing a work sequence**, rather than assuming that a more detailed workflow is better.

In the FLT campaign, a subgoal could have an upper-level use that an agent could not discover through the available query interface. Treating shared information primarily as an experience library could also focus design on storage, retrieval, and reuse while overlooking tentative ideas, requests for help, and candidate routes. Later trace analysis required further distinctions between information existing, reaching an agent, being used, and contributing to collective progress.

These experiences expanded the question from designing a better environment to asking whether a system can recognize and overcome limitations of its own design. See [the development narrative](research-development.md); the project cards retain the concrete cases and evidence limits.

## Current direction

Formal proof offers expressible goals, dependencies, and verification feedback, but not a ready-made organization. I want to combine system experiments and mathematical modeling to study autonomous system-level exploration and sustained evolution: discovering and retaining useful changes, allocating resources between task work and improvement, preserving multiple evolutionary directions, and testing when changes genuinely expand collective capability.

Shared memory, tool interfaces, and research-state representations are possible entry points, **not the predetermined scope of the whole agenda**. No result here establishes effective system-level autonomous evolution. See [the future direction](docs/research-plan.md) and [current questions](current-questions.md).

## Tools, prototypes, and full index

[Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) and [pi-lean-tools](projects/pi-lean-tools.md) support the Putnam experiments; they are not additional independent results. Metron, Persistent Mathematical Worlds, MathWeave, PMW Research Platform, and Aperture explore state, persistence, and organizational boundaries; see [the research graph](docs/research-graph.md). [oncewhere](projects/oncewhere.md) remains an adjacent creative work, not a mathematical-system component.

<details>
<summary>Full index: projects, tools, stage outputs, and associated references</summary>

Entries are not counts of independent projects or papers. Status and evidence reflect each entry's last review; source access uses `visibility_last_checked` where recorded. Evidence and contribution details are in each card. `ContextSwarmJudge` is reference-only, not a repository contribution of mine.

<!-- project-index:start -->
| Entry | Status | My role | Original source |
| --- | --- | --- | --- |
| [Collective Acceleration](projects/collective-acceleration.md) | Analysis | Direct work | Internal material |
| [Putnam 2025: formal proof experiments](projects/putnam-2025.md) | Experiment recorded | Direct work | Private source |
| [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) | Experiment recorded | Direct work | Private source |
| [Pi Lean Tools](projects/pi-lean-tools.md) | Prototype | Direct work | Public source |
| [ContextSwarm](projects/contextswarm.md) | Collaborative research | Team contribution | Private source |
| [ContextSwarmJudge](projects/contextswarm-judge.md) | Associated component | Reference only; no repository contribution | Private source |
| [ICLR 2027 stage output: FLT system and FLTBench](projects/flt-iclr-stage-output.md) | Submitted | Team contribution | Internal material |
| [FLT campaign: collaboration analysis (AAMAS 2027)](projects/flt-proof-weaving-aamas.md) | Submitted | Team contribution | Internal material |
| [Metron](projects/metron.md) | Prototype | Direct work | Private source |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md) | Prototype | Direct work | Private source |
| [MathWeave](projects/mathweave.md) | Implemented | Direct work | Private source |
| [PMW Research Platform](projects/pmw-research-platform.md) | Prototype | Direct work | Private source |
| [Rights in the Exponent](projects/rights-in-the-exponent.md) | Analysis | Direct work | Private source |
| [Aperture](projects/aperture.md) | Prototype | Direct work | Private source |
| [Agent Math Frontier](projects/agent-math-frontier.md) | Implemented | Direct work | Public source |
| [oncewhere](projects/oncewhere.md) | Adjacent creative work | Direct work | Public source |
| [Trace analysis](projects/trace-analysis.md) | Research thread | Direct work | Internal material |
| [TacticWorld](projects/tacticworld.md) | Research design | Direct work | Private source |
<!-- project-index:end -->

</details>

## Maintaining the map

For a new artifact, record its question, actual work, strongest evidence, and limits before updating its card and `project-index.json`. Keep `current-questions.md` and `question-index.json` aligned. Do not rewrite history merely to preserve a tidy trajectory.

```bash
python scripts/build_index.py --write
python scripts/build_index.py --check
python -m unittest discover -s tests -v
```

[Card template](docs/project-card-template.md) · [Evidence and status](docs/evidence-and-status.md) · [Revision decision](decisions/0003-scope-contribution-and-reader-path.md)
