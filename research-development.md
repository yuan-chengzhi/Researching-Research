# Research development

## Why this document exists

This document records how my research question changed in practice. It is deliberately not a story in which I planned a complete multi-agent architecture first and then implemented it. The later idea of an evolving research substrate grew out of smaller experiments whose original questions were narrower.

The stable question has been:

> How can I build an environment that lets an AI agent use its mathematical ability, preserve useful work, and continue from it when the task, session, or agent changes?

What changed was the scale and meaning of environment: tools and local feedback, then long action loops, shared state, unfinished-work representation, persistent research worlds, and finally the possibility that the substrate itself should be changed by evidence.

## The trajectory

| Stage | Question at the time | Intervention | Observation or limit | Question after the experiment |
| --- | --- | --- | --- | --- |
| Putnam 2025 | What can one agent do on a difficult, formally checkable mathematical task? | Start from concrete Putnam problems and a strict formal environment. | A result is only interpretable when attempts, feedback, and checking can be inspected. | How can an agent keep trying rather than stop at its first plausible attempt? |
| Pi Math First Proof Swarm and Ralph loop | How can an agent repeatedly act, receive feedback, recover from failure, and use its available mathematical ability? | Repeated fresh-context attempts, local verifier feedback, recovery, and matched experiments. | More steps alone are not enough; the action-to-feedback environment is part of the research object. | Which tools and feedback signals make long attempts useful? |
| Pi Lean Tools | How can an agent work with Lean without being blocked by names, APIs, diagnostics, or cold starts? | Advisory checks and snippets, declaration/premise/tactic search, error explanations, caching, and a persistent REPL. | Tool output can reduce friction, but it must not be presented as proof authority. Final verification remains separate. | What should be shared when more than one agent works on the same problem? |
| Multi-agent work, ContextSwarm, and FLT | How can many local activities become cumulative mathematical progress? | Proof-state handling, traces, shared state, handoffs, and analysis of reuse and coordination. | Parallel activity, communication, and token volume do not automatically become a reusable proof state. | Which objects, links, failures, and evidence should a successor inherit? |
| Metron | How should active routes, certificates, unresolved obligations, failures, and repeated work be represented? | Structured unfinished state, temporal evidence, replay, and explicit distinctions between activity and mathematical validity. | Unfinished work cannot be reduced safely to one progress number. | What kind of persistent world can preserve this distinction? |
| Persistent Mathematical Worlds and MathWeave | What heterogeneous objects should a research world store, and how should they be linked and admitted? | Typed state, provenance, versions, append-only records, derived views, and admission boundaries. | Retrieval is not admission; a map is not a proof; provisional material must remain visibly provisional. | How can agents and runtimes be replaced without silently changing the meaning of the work? |
| PMW Research Platform, Rights in the Exponent, and Aperture | What does replacement mean when state, permissions, runtimes, and organizations change? | Explicit lifecycle and replaceability boundaries. | Replaceability has levels and contracts; it is not one binary property. | Can the organization of proof work itself become an experimental variable? |
| Current hypothesis | Can the objects, links, admission rules, protocols, and challenge selection of a proof-work substrate evolve from traces? | Use training tasks for proposals and comparisons, preserve a stable verification boundary, and evaluate on frozen held-out tasks. | This is a research hypothesis, not a result. It must earn its claim through a controlled experiment. | Which substrate mutations transfer to unseen tasks and replacement agents without laundering stale evidence? |

## What did not change

I did not begin by deciding to build a large swarm or a universal workflow. The persistent idea was to improve the environment around the agent so that its mathematical capability could be used more fully. In the early stage, environment meant loops, tools, local checks, and time. In the later stage, it also meant state, evidence, provenance, links, and the ability to inherit work.

This is why Pi Math First Proof Swarm, Ralph loop, and Pi Lean Tools belong at the beginning of the story. They are not preliminary implementation details that can be skipped in favour of the final abstraction. They are the experiments that made the abstraction possible.

## Why formal mathematics is the first setting

Formal mathematics is a useful first laboratory because a Lean proof can be checked relative to an explicit formal statement, and the relevant files, commands, diagnostics, and versions can be replayed. This gives long-horizon experiments a precise local authority.

That authority has a boundary. Kernel acceptance does not by itself establish that an informal statement was translated faithfully, that the chosen definitions express the intended mathematics, that the result is important, or that the proof is reusable by a later researcher. Those gaps are part of the reason to study the substrate: the system must preserve both formal artifacts and the evidence connecting them to the surrounding research process.

If proof production becomes cheaper, the scarce work may move toward selecting, understanding, explaining, canonicalizing, admitting, maintaining, and reusing proofs. The aim is therefore not only to make one proof pass. It is to make formal mathematical work discoverable, checkable, inheritable, and diagnosable over longer episodes.

## The next question

The next question is not whether a self-modifying swarm sounds plausible. It is whether a narrowly defined substrate change has a measurable and transferable effect:

> With the model, budget, Lean toolchain, verifier, and test set fixed, can a research substrate learn from training traces which objects to store, how to link them, and when to make them inheritable, while improving continuation or reuse on held-out mathematical tasks?

The answer could be negative. A useful result could be that richer state adds cost without transfer, or that only a small stable protocol helps. The repository should preserve those outcomes as changes in the research question rather than smoothing them into a success narrative.

## The place of oncewhere

oncewhere is an adjacent creative work, not a component of the formal-mathematics system. It belongs in the atlas because it carries the same personal concern into another medium: after an immediate experience ends, what can remain returnable, interpretable, and alive? Its relationship to the mathematical projects is thematic and personal, not evidence that the two systems share a technical mechanism.