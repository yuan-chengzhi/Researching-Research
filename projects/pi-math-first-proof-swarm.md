---
id: pi-math-first-proof-swarm
title: Pi Math First Proof Swarm
theme: reliable-action-and-feedback
status: experimentally-observed
visibility: private
repository: https://github.com/yuan-chengzhi/pi-math-first-proof-swarm
last_reviewed: 2026-10-11
---

# Pi Math First Proof Swarm

## At the time

This began with Putnam 2025 and a smaller question than "how should a large swarm be organized?": what can an agent do on a difficult formal-mathematics task if it is given a loop that lets it act, check, retry, and recover? The swarm apparatus came from trying to answer that question with repeated, inspectable attempts.

## Question

Can a formal-first agent setup preserve enough local feedback and experiment structure for a long attempt to be inspected later?

## What exists

The repository contains a formal-first swarm apparatus and an experiment branch, experiment/e13, used to study a full Putnam 2025 report. The important object is not a single headline number but the preserved relationship between prompts, proof attempts, tool feedback, verification, and the final report.

## My role

My contributions have centred on prompt design, proof-state optimisation, experiment analysis, and issue fixing. The card separates those contributions from the complete repository history.

## Evidence

Use the [repository](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm) and the [experiment/e13 branch](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/tree/experiment/e13). A fixed experiment commit will be added after the branch is audited again.

## What this establishes

The experiment provides evidence that formal feedback can be placed inside a repeatable experiment and that results can be reviewed at the level of individual attempts.

## What this does not establish

A successful formal experiment does not establish general mathematical research ability, broad theorem-proving autonomy, or a universal recipe for swarm design.

## Belief before → observation → belief after

- **Before:** the main bottleneck might be whether a model can produce the right proof move.
- **Observation:** retries, verifier signals, failure recovery, and the surrounding apparatus changed what an agent could do and what could be diagnosed.
- **After:** the environment around the agent is itself a research variable; prescriptive roles should not be assumed to be the best organization.

## Retrospective relation

This project is the origin of the later research question, but it was not an implementation of the evolving-substrate agenda. The larger questions about shared state, unfinished work, and persistence grew out of later experiments.

## Next question

Which feedback and review choices explain the differences between attempts, and which of them transfer to later research worlds?