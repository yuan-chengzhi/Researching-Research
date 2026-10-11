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

Local inspection alone does not solve retrieval, strategy selection, theorem discovery, or long-horizon coordination.

## What changed in my research direction

It clarified that tool use is part of the research design. The question is not only whether an agent can call a tool, but whether the tool returns the kind of state another agent can inherit.

## Next question

Which probes are stable enough to become a reusable contract between replaceable research sessions?
