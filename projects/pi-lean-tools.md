---
id: pi-lean-tools
title: Pi Lean Tools
theme: reliable-action-and-feedback
status: prototype
visibility: private
repository: https://github.com/yuan-chengzhi/pi-lean-tools
last_reviewed: 2026-10-11
---

# Pi Lean Tools

## At the time

After the first Putnam and Ralph-style loops, the problem was not yet multi-agent organization. It was that an agent could have useful mathematical ability while being slowed by Lean names, APIs, diagnostics, retrieval, and cold starts. I treated the tool environment as a way to release that ability rather than as a substitute for mathematical judgment.

## Question

What should a mathematical agent be able to inspect immediately after it changes a Lean proof state?

## What exists

The repository develops Lean-aware local probes, including a frontier-probe direction in codex/frontier-probe-command. The emphasis is on short, toolchain-aware feedback rather than a large opaque wrapper.

## My role

I worked on prompt and tool design, proof-state handling, and the analysis of failure cases. The project is a feedback-loop investigation, not a claim that every useful mathematical operation has been automated.

## Evidence

Use the [repository](https://github.com/yuan-chengzhi/pi-lean-tools) and the [frontier-probe branch](https://github.com/yuan-chengzhi/pi-lean-tools/tree/codex/frontier-probe-command). The next review should pin the branch head for the specific probe implementation.

## What this establishes

A small Lean-aware probe can shorten the distance between an attempted action and a checkable local consequence.

## What this does not establish

Local inspection alone does not solve retrieval, strategy selection, theorem discovery, or long-horizon coordination. Advisory tool output is not proof evidence; final verification remains the authority.

## Belief before → observation → belief after

- **Before:** improving the local action environment might be enough to unlock more of an agent's existing capability.
- **Observation:** probes, caches, and a persistent REPL reduce friction, but they do not decide what should be shared or how a later agent should interpret a route.
- **After:** the environment must include inheritable research state, not only better calls to Lean.

## Retrospective relation

Pi Lean Tools is an enabling layer for the later multi-agent and persistent-state questions. It is deliberately not presented as a solved single-agent harness or as the final research object.

## Next question

Which probes are stable enough to become a reusable contract between replaceable research sessions?