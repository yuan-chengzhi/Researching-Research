# Future direction: collective capability and system-level autonomous evolution

[中文](research-plan.zh-CN.md) · [Development](../research-development.md) · [Current questions](../current-questions.md)

> This is a research direction, not a completed system or an established improvement. Existing prototypes are entry points, not implementations of the full agenda.

## Where the question comes from

I want AI to support more complex mathematical research and to understand how many agents' local explorations become collective progress. Formal tasks offer goals, dependencies, and verification feedback. Yet shared state, tool interfaces, and prompts still embody designers' assumptions about research. An experience-library framing encourages work on storage, retrieval, and reuse; a task-allocation framing can gradually become a prescribed workflow. These choices may be useful, but must remain open to experiment.

The central question is whether an Agent Swarm can autonomously discover design opportunities, propose, implement, test, and retain useful changes, then improve how it searches for and evaluates changes—possibly discovering effective organizations its designers did not anticipate.

## Modifiability is not effective evolution

Permission to edit tools or prompts only establishes that change is possible. Effective evolution also requires finding worthwhile problems, paying the cost of improvement alongside task work, resisting changes that merely exploit the evaluator, and obtaining repeatable benefits on subsequent independent tasks.

I am interested in how task-solving and improvement teams should coordinate or separate, what context they should share, and when several competing design directions can avoid premature convergence. Multiple teams or competing strategies are possibilities to investigate, not a predetermined architecture.

## Experiments and mathematical models

Formal mathematics is the main initial setting, not a presumed limit on eventual applicability. Shared information, proof state, tools, communication, work allocation, and evaluation procedures may all be research objects. Each experiment needs a bounded comparison; that does not reduce the whole agenda to modifying shared memory.

Evaluation should account for discovery, implementation, testing, and maintenance costs. Suitable comparisons may include a static system, additional information, or equivalent extra search under stated resource and evaluation conditions. Repeated runs, subsequent independent tasks, and varied organizational conditions can test transfer. The exact protocol should follow the question rather than committing now to one mutation family or a fixed four-arm experiment.

Mathematical models can isolate relationships among information propagation, division of work, feedback, and search diversity; actual runs can reveal omitted mechanisms. Completion and cost should be studied alongside errors, dependencies, artifact continuity, and failure processes rather than treating one number as the whole research outcome.

## Connection to existing work

Putnam offers experience with tools and work sequences. ContextSwarm and its AAMAS analysis expose gaps between local activity, shared state, and global progress. Metron, persistent-world, and replaceability prototypes provide some concrete experimental objects. Together they motivate the question, but do not establish autonomous evolution. Applicability beyond mathematics remains to be tested.
