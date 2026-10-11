---
id: flt-proof-weaving-aamas
title: What Can the Next Agent Build On? Proof Weaving in an FLT Campaign
theme: evidence-and-diagnosis
status: analysis
visibility: internal
repository: internal:flt-proof-weaving-aamas
last_reviewed: 2026-10-11
period: AAMAS 2027 analysis stage
kind: paper-output
ownership: collaborative
role_scope: trace-analysis-and-manuscript-revision
contribution_scope:
  - execution-trace and experiment-data organization
  - case analysis of mathematical progress and system behaviour
  - analysis of ProofState, CPS, feedback, and shared-state breaks
  - figures and visual analysis
  - proofreading and manuscript revisions
not_my_contribution:
  - the complete FLT system implementation
  - the original ownership of every run component
---

# What Can the Next Agent Build On? Proof Weaving in an FLT Campaign

## Place in the trajectory

This is the later AAMAS analysis branch of the same FLT campaign. It studies what the large run left behind for a later agent, rather than presenting a second system-building project.

## What exists

The analysis organizes and interprets execution traces and experiment data from a large FLT formalization run, reported at approximately 100B tokens, 40K aggregate agent-hours, and 128 of 1024 available slots. The paper title is *What Can the Next Agent Build On? Proof Weaving in an FLT Campaign*.

## My role

I organized and analyzed the traces and experimental data, extracted cases of mathematical progress and system behaviour, examined the relationships among ProofState, CPS, feedback, and shared-state breaks, prepared figures, and contributed proofreading and manuscript revisions.

## What this establishes

The analysis makes it possible to distinguish local activity, formal verification, shared state, and the evidence that a later agent can actually use. It turns the run's traces into a bounded account of what the system did and where continuity failed.

## What this does not establish

Trace analysis alone does not provide a universal causal explanation of swarm outcomes, and the paper does not turn the unfinished FLT campaign into a completed formalization.

## What changed in my research direction

The central question shifted from how to run more agents to what a later agent can safely build on. That shift motivates the proposed research-substrate direction, while leaving its system and experiments to future work.

## Next question

Which representations, relations, and use protocols can be improved from run evidence without allowing stale or unsupported material to be inherited?
