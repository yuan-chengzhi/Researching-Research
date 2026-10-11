---
id: putnam-2025
title: Putnam 2025 formal-first run
theme: reliable-action-and-feedback
status: experimentally-observed
visibility: private
repository: https://github.com/yuan-chengzhi/pi-math-first-proof-swarm
last_reviewed: 2026-10-11
period: Putnam 2025
---

# Putnam 2025 formal-first run

## Question at the time

What can a formal-first agent setup do on a difficult mathematical task when it can act, check, retry, and recover?

## What exists

The run used Pi Math First Proof Swarm, Pi Lean Tools, and a Ralph-style loop to study all 12 Putnam 2025 problems. Each problem received eight parallel attempts. The full run took approximately 5.5 hours.

## My role

I worked on the formal-first setup, including prompt and experiment design, proof-state handling, the Lean-aware tool environment, and analysis of the resulting attempts.

## Result and boundary

All 12 problems reached `final_verified` in the internal experiment pipeline. Here `final_verified` is the run's own formal verification criterion; it is not an official Putnam contest score and does not establish general mathematical research ability.

## What this establishes

The run provides a concrete starting point for studying how tools, local verification, retries, and experiment structure affect an agent's work on formal mathematical tasks.

## What this does not establish

It does not establish a full theorem-proving system, broad mathematical autonomy, or a universal recipe for organizing agents.

## What changed in my research direction

The result made the surrounding environment a first-class research variable. The next question was not simply whether an agent could solve a task, but what later work could inspect, reuse, and improve.

## Next question

Which feedback and review choices explain the differences between attempts, and which of them remain useful when the work becomes longer and more collaborative?
