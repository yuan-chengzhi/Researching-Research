# Research development

[中文](research-development.zh-CN.md) · [Home](README.md) · [Current direction](docs/research-plan.md)

This narrative follows changes in questions, not a predetermined technical pipeline. Some projects continued earlier work; others were parallel explorations. “Putnam 2025” identifies the problem set, not the date of the experiments.

## Progress sharing and the persistence of actual work

In [Collective Acceleration](projects/collective-acceleration.md), I modeled individual progress, reset, and neighbor maximum-progress synchronization as a stochastic process. This trained a state-and-network view of collective behavior, while exposing an omitted distinction: restarting an attempt need not erase external records. Propagation, preservation, retrieval, and continuation are different questions. The original report is not bundled; the card preserves an author summary rather than inventing unaudited formulas.

## Putnam: capabilities versus prescribed order

The Putnam experiments involved a formal proof loop, repeated attempts and recovery, and Lean-aware tools. The question expanded from whether the model could solve a problem to whether its environment supplied timely checks, correction, and continued attempts.

In the A5 prompt comparison, both settings completed the proof after runtime and tool problems were repaired. The setting without added natural-language-first guidance also chose to reason first. One comparison cannot establish a universally best workflow, but it made work sequence itself an experimental choice.

The E13 report dated 2026-06-22 records twelve internal verification results and a verifier signature-check problem behind repeated candidate rejection. Apparent repeated failure therefore required diagnosis along the tool-and-feedback path, not attribution to mathematical ability alone. The [project card](projects/putnam-2025.md) retains pinned evidence and runtime definitions.

## FLT: reconnecting local results to the shared proof

ContextSwarm made the setting longer-horizon and collaborative. ProofState goals, routes, dependencies, and verification status interacted with CPS research information to shape what agents could see and continue.

My focus was relating local results to upper-level proof needs. In one case, a subgoal already had two parent routes, but the available interface could not query them from the child. I diagnosed and advocated the missing query. Other work included FLTBench reference access, prompt restructuring, and exploration of links between research records and multiple mathematical objects. The [ContextSwarm card](projects/contextswarm.md) distinguishes implementation, exploration, and author-reported evidence.

The team system, FLTBench, and ICLR submission, followed by AAMAS run analysis, are different outputs of the same campaign. Full FLT formalization remained unfinished. Neither the whole team system nor the associated Judge repository is claimed as my individual implementation.

## Large-run analysis: observations and explanations

AAMAS analysis required reconstruction by proof object, candidate version, shared record, and verification event, using relationships available at the time. A later relationship must not be projected onto earlier behavior. Similar errors recurring can involve different mechanisms: feedback not yet delivered, records not used, or altered candidates.

My work included trace and data analysis, cases, diagnostic-method notes, selected visualizations, and manuscript revisions. This separated the claims that an object existed, an agent encountered it, later work used it, and it produced repeatable benefit. Each needs different evidence.

## Prototypes and parallel explorations

| Work | Question | Boundary |
| --- | --- | --- |
| [Metron](projects/metron.md) | How should active routes, certificates, and unfinished obligations coexist? | A prototype, not a universal progress measure. |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md), [MathWeave](projects/mathweave.md) | How should state persist, and how should records, retrieved views, and accepted results differ? | Implementation is not evidence of reuse benefit by itself. |
| [PMW Research Platform](projects/pmw-research-platform.md), [Aperture](projects/aperture.md), [Rights in the Exponent](projects/rights-in-the-exponent.md) | What constrains replacement of sessions, permissions, components, and organizations? | Different designs, implementations, and analyses, not one mature platform. |
| [TacticWorld](projects/tacticworld.md) | Can alternative actions' consequences provide better learning signals? | A parallel July 2026 exploration; complete training and evaluation unfinished. |
| [Agent Math Frontier](projects/agent-math-frontier.md), [Trace analysis](projects/trace-analysis.md) | How should different evidence and failures change the next question? | Evidence organization is not a universal causal explanation. |

[oncewhere](projects/oncewhere.md) remains adjacent: a creative exploration of preserving and returning to shared experience, not a technical component.

## Current transition: the limits of the design itself

An experience-library framing can keep attention on storage and retrieval; a task-allocation framing can accumulate prescribed steps. Recognizing that tendency made me examine assumptions in tool interfaces, object types, and prompts.

The next question is not only how work should be preserved or inherited. It is whether the system can discover design opportunities, test and retain improvements, and eventually change its own improvement procedures. Shared memory and research state remain useful slices, not the whole direction. The [current direction](docs/research-plan.md) states the broader agenda and its open evidence requirements without erasing the earlier slices or presenting them as completed system-level results.
