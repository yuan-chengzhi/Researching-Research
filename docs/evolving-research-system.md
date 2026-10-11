# Evolving proof-work substrate

> Status: research hypothesis and experiment agenda. This document does not describe a completed system.

## Scope

I am not proposing to evolve model weights as the first research object, and I am not treating a better single-agent harness as the final question. Those can be useful controls or enabling mechanisms. The intended unit is the research substrate around a group of agents doing formal mathematics: what is stored, how it is connected, what can be inherited, and how the next challenge is selected.

The motivating distinction is between a proof that passes a verifier and research work that another agent can safely continue. The latter requires formal artifacts, process evidence, provenance, negative results, and explicit admission boundaries.

## Three coupled components

### Proof-world substrate

Agents work in a Lean environment and produce or modify formal artifacts. The substrate records statements, definitions, goals, subgoals, candidate lemmas, certificates, unresolved obligations, scripts, code, tool observations, diagnostics, attempts, handoffs, and versions.

### Research-system evolution

Training traces and verdicts can be used to propose and compare changes to object schemas, links, admission rules, retrieval views, context packaging, tools, routing, handoffs, and agent organization. A proposal is a versioned mutation with a diff, a reason, a replayable evaluation, and a rollback point. A mutation is not promoted merely because it improves the training score.

### Challenge frontier

Failures and bottlenecks can motivate new formal tasks with longer dependencies, harder reuse, or greater coordination demands. The curriculum may change on the training side. The holdout set must remain sealed until evaluation.

## A candidate formalization

At a given time, describe the substrate as E_t = (O_t, L_t, P_t, G_t, V_t):

- O_t: typed mathematical, process, and system objects;
- L_t: typed links with evidence and admission conditions;
- P_t: agent and tool interaction protocols;
- G_t: task and curriculum generation;
- V_t: diagnosis, evaluation, and verification interfaces.

Each run produces an append-only event log. Events carry artifact identity, exact version, agent or tool, goal, operation, feedback, admission status, and evaluator version. Retrieval exposure is recorded separately from mathematical validity.

## Stable core and evolving layer

Some boundaries should be stable before evolution begins:

- trusted Lean checking and an explicit formal-statement boundary;
- immutable artifact identity and version lineage;
- provenance and replayable event logs;
- explicit states such as candidate, checked, accepted, rejected, and stale;
- a frozen holdout harness and contamination boundary;
- no automatic promotion from a training success to a scientific claim.

Other parts are candidates for controlled evolution:

- object schema extensions and removals;
- semantic, structural, epistemic, operational, provenance, and retrieval links;
- admission and staleness policies;
- context compilation and retrieval exposure;
- handoff, compaction, and routing;
- the agent population and task curriculum.

The point is not to freeze an imagined human organization. It is to freeze the authority and audit boundary while making organizational hypotheses comparable.

## Minimum experiment

Start with one mutation family, such as typed-state admission or retrieval exposure. Hold the model, Lean snapshot, task budget, verifier, and agent protocol fixed. Compare:

1. no persistent state;
2. ordinary text sharing;
3. a fixed typed provenance substrate;
4. a substrate whose selected schema or admission policy is evolved on training tasks.

Evaluate research episodes rather than only isolated proof attempts: interruption, replacement-agent continuation, unresolved-obligation reduction, and reuse on a disjoint task. Record valid proof rate, time to certificate, repair cost, duplicate work, accepted-artifact reuse, stale inheritance, admission errors, token and Lean cost, schema churn, rollback, and transfer to holdout tasks.

A convincing result requires improvement on held-out tasks without a material increase in stale or invalid inheritance. Training-only gains count as overfitting until they transfer.

## What could falsify the agenda

The agenda should be revised if richer state never improves continuation, if evolution only learns benchmark-specific shortcuts, if provenance costs dominate any reuse benefit, or if protocol changes cannot be replayed and compared. A negative result would still answer the central question by locating the boundary of useful substrate design.