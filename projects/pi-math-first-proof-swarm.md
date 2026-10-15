---
id: pi-math-first-proof-swarm
title: "Pi Math First Proof Swarm"
theme: reliable-action-and-feedback
status: experimentally-observed
visibility: private
ownership: direct
repository: https://github.com/yuan-chengzhi/pi-math-first-proof-swarm
last_reviewed: 2026-10-14
---

# Pi Math First Proof Swarm

This is the experiment apparatus behind the [Putnam 2025 project](putnam-2025.md), not a second independent result to add to the same 12-problem run.

## Question and implementation

Can an agent repeatedly attempt formal proof work, inspect feedback, recover from interruption, and submit a candidate to a separate verifier? The repository contains proof-control objects, attempt execution, local checking, advisory context, and final-verification handoff. My work includes experiment and prompt design, Lean-tool integration, runtime diagnosis, and result analysis, with AI coding assistance.

## Evidence

The experiment snapshot is pinned to `20c6e0342654265ad47f5c3c63fd9a013100232a`. See the [E13 report](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/docs/thoughts/e13-putnam2025-full12-formal-sweep-zh.md), [A5 prompt comparison](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/docs/thoughts/e12a-nlfirst-vs-formal-analysis-zh.md), and [implementation overview](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/README.md). These are private-source records, not an independent rerun performed by this atlas.

The [Putnam project card](putnam-2025.md) owns the result wording, runtime denominator, and limitations. Keeping them there avoids counting an experiment and its tools as separate achievements.

## What changed

The question expanded from whether the model could produce a proof move to how the surrounding tools, feedback, recovery, and prompts shape its work. Prescribed order became a choice to test rather than an assumed requirement. These observations motivate later organizational questions; they do not establish a universal swarm design or an already self-evolving system.
