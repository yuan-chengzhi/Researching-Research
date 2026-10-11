# Researching Research

## A personal research trajectory in AI for Mathematics

This is a living atlas of how my research question developed from a concrete Putnam 2025 formal-first run into a question about evolving research substrates.

I did not begin by deciding to build a large agent swarm. I began with a smaller question: if an agent is given a sufficiently good formal-mathematics environment, can its mathematical ability become reliable work? In one full Putnam run, 12 problems received eight parallel attempts each in approximately 5.5 hours, and all 12 reached the run's internal `final_verified` criterion. Pi Math First Proof Swarm, the Ralph loop, and Pi Lean Tools were the tools and experiments through which I studied that environment.

The central transition was the FLT formalization campaign. I worked on ProofState and CPS-related tools, prompts, experiment execution, FLTBench issues, and system-level evaluation. The campaign produced an ICLR-stage system-and-benchmark submission and a later AAMAS analysis of the large run; the two outputs are branches of one project, and the overall FLT formalization remained unfinished.

As the work expanded to multiple agents, the meaning of environment expanded as well: shared state, proof objects, unfinished routes, provenance, handoffs, and admission. The current direction asks whether these objects and protocols can themselves be changed by experimental evidence while formal authority and held-out evaluation remain fixed.

The stable interest is not a pre-written workflow. It is to build environments in which agents can use, preserve, and continue mathematical capability. This repository records the changes in that question, including the limits and negative evidence that caused it to change.

## Why formal mathematics

Formal proof is a useful first laboratory because Lean can check a proof relative to an explicit formal statement, while files, tool calls, diagnostics, and versions can be replayed. It does not solve statement fidelity, definition choice, library access, explanation, or research value. Those boundaries are part of the research problem.

## Next direction

The next question is whether the environment around formal mathematical agents can improve through small, verifier-grounded experiments: what should be preserved, how should evidence be linked, and what may a later agent safely inherit? This is a research direction, not a completed system. See the short [research plan](docs/research-plan.md); new artifacts will be added to the atlas as the work continues.

## How to read this repository

1. Start with [the research development history](research-development.md).
2. Read [the research graph](docs/research-graph.md) to see how projects, questions, transitions, and evidence connect.
3. Read [the current research arc](research-arc.md), then [the current questions](current-questions.md).
4. Open a project card for the question, evidence, my role, and limits of the result.
5. Use fixed commit links when you need to audit a historical claim.
6. Read [the evidence and status contract](docs/evidence-and-status.md) before comparing projects.

## Project scope

The project index distinguishes direct and collaborative work. Direct entries are repositories and artifacts I built directly, or built with Codex or Claude Code. Collaborative entries are included when I have a real research role and an auditable contribution boundary; they are never presented as individually authored systems.

## Research map

| Theme | Question | Representative work |
| --- | --- | --- |
| Reliable action and feedback | Can an agent make a mathematical move and receive a trustworthy local signal? | [Putnam 2025 formal-first run](projects/putnam-2025.md), [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md), [Pi Lean Tools](projects/pi-lean-tools.md) |
| FLT formalization and benchmark | How can a long formalization campaign make progress and its limits inspectable? | [ContextSwarm — FLT formalization system and FLTBench](projects/contextswarm.md), [ICLR 2027 stage output](projects/flt-iclr-stage-output.md), [AAMAS run analysis](projects/flt-proof-weaving-aamas.md), [ContextSwarmJudge](projects/contextswarm-judge.md) (associated verification layer) |
| Unfinished mathematical work | How should active attempts, valid certificates, and unresolved obligations coexist? | [Metron](projects/metron.md) |
| Persistent research worlds | Can research state survive replacement of agents and sessions without turning provisional material into truth? | [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md), [MathWeave](projects/mathweave.md) |
| Organization and replaceability | What does a research organization control, and what does replacement actually mean? | [PMW Research Platform](projects/pmw-research-platform.md), [Aperture](projects/aperture.md), [Rights in the Exponent](projects/rights-in-the-exponent.md) |
| Evidence and diagnosis | How can we explain a swarm's outcome without collapsing evidence into a single score? | [ContextSwarmJudge](projects/contextswarm-judge.md) (collaborative), [Agent Math Frontier](projects/agent-math-frontier.md), [Trace analysis](projects/trace-analysis.md) |
| Adjacent creative work | What does it mean to preserve a shared experience as something that can be revisited? | [oncewhere](projects/oncewhere.md) |

## Selected work

<!-- project-index:start -->
| Project | Theme | Status | Ownership | Visibility | Evidence |
| --- | --- | --- | --- | --- | --- |
| [Putnam 2025 formal-first run](projects/putnam-2025.md) | reliable-action-and-feedback | experimentally-observed | direct | private | 12 problems; 8 parallel attempts per problem; approximately 5.5 hours; all 12 final_verified by the internal pipeline |
| [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) | reliable-action-and-feedback | experimentally-observed | direct | private | branch experiment/e13; fixed commit to be pinned after branch audit |
| [Pi Lean Tools](projects/pi-lean-tools.md) | reliable-action-and-feedback | prototype | direct | private | branch codex/frontier-probe-command; fixed commit to be pinned after branch audit |
| [ContextSwarm](projects/contextswarm.md) | formal-proof-systems | collaborative-research | collaborative | private | https://github.com/nustarai/ContextSwarm/commit/1076e4e8a6d194870bbf0ce65303fbad8dd2a7e3; FLTBench task and run artifacts; ICLR 2027 submission materials (internal) |
| [ContextSwarmJudge](projects/contextswarm-judge.md) | evidence-and-diagnosis | collaborative-research | collaborative | private | https://github.com/nustarai/ContextSwarmJudge/commit/33f9ca5ea75f054b94eacbfc12f79854d32b0336 |
| [ICLR 2027 stage output: FLT system and FLTBench](projects/flt-iclr-stage-output.md) | formal-proof-systems | submitted | collaborative | internal | ICLR 2027 submission materials (internal) |
| [What Can the Next Agent Build On? Proof Weaving in an FLT Campaign](projects/flt-proof-weaving-aamas.md) | evidence-and-diagnosis | analysis | collaborative | internal | internal execution-trace and experiment-data analysis; AAMAS 2027 manuscript materials |
| [Metron](projects/metron.md) | unfinished-mathematical-work | prototype | direct | private | branch metron/f0-runtime-v2; fixed commit to be pinned after branch audit |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md) | persistent-research-worlds | prototype | direct | private | https://github.com/yuan-chengzhi/persistent-mathematical-worlds/blob/codex/c07-apparatus-fix/docs/decisions/0004-polycentric-agenda-direction.md |
| [MathWeave](projects/mathweave.md) | persistent-research-worlds | implemented | direct | private | https://github.com/yuan-chengzhi/MathWeave/commit/393fca141df3aa990378edb53fa3cc9e89445011 |
| [PMW Research Platform](projects/pmw-research-platform.md) | organization-and-replaceability | prototype | direct | private | https://github.com/yuan-chengzhi/pmw-research-platform/commit/d28748c8a8a67d19b17ccbd347b8c5a853c33782 |
| [Rights in the Exponent](projects/rights-in-the-exponent.md) | organization-and-replaceability | analysis | direct | private | https://github.com/yuan-chengzhi/rights-in-the-exponent/commit/2b7291c564d609a68d580f5279af4c3c8ee27136 |
| [Aperture](projects/aperture.md) | organization-and-replaceability | prototype | direct | private | https://github.com/yuan-chengzhi/aperture-worlds/commit/5e72b0b1859bee3ae71babbecf6eadd20c9061bc |
| [Agent Math Frontier](projects/agent-math-frontier.md) | evidence-and-diagnosis | implemented | direct | public | https://github.com/yuan-chengzhi/agent-math-frontier/commit/e5fb06928f26e0762e62c17b2cea241c29c40918 |
| [oncewhere](projects/oncewhere.md) | adjacent-creative-work | adjacent-work | direct | private | https://github.com/yuan-chengzhi/oncewhere/commit/9ea4c02316cdd96ca5c4f8f6d7a0af2bdcfe2402 |
| [Trace analysis](projects/trace-analysis.md) | evidence-and-diagnosis | research-thread | direct | internal | analysis thread; repository link will be added if the apparatus becomes a standalone project |
<!-- project-index:end -->

## My role in the work

The cards distinguish the existence of a repository from my contribution to it. In the FLT campaign, the cards separate system and benchmark work from the later AAMAS trace analysis and manuscript revisions. Across the mathematical-agent projects, my work has included prompt and experiment design, proof-state optimisation, trace analysis, issue fixing, data analysis, figures, proofreading, and revisions.

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
