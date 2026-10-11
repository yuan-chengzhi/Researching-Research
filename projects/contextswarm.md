---
id: contextswarm
title: ContextSwarm
theme: formal-proof-systems
status: collaborative-research
visibility: private
ownership: collaborative
role_scope: system-tools-and-experiment-analysis
repository: https://github.com/nustarai/ContextSwarm
last_reviewed: 2026-10-11
period: FLT formalization campaign / ICLR stage
---

# ContextSwarm: FLT formalization system and FLTBench

## Question at the time

How can a large collection of mathematical agents communicate, verify local work, and accumulate measurable progress on the formalization of Fermat's Last Theorem?

## What exists

ContextSwarm is the core collaborative project behind the FLT formalization campaign. It built and evaluated the large-scale formal-proof system and established FLTBench as a benchmark of ten Lean reconstruction tasks. The project produced an ICLR 2027 stage submission. The overall FLT formalization target remained unfinished; the system, benchmark, and evidence about where progress stopped are therefore part of the result.

## My contribution

I optimized ProofState and CPS-related tools, improved prompts and experiment-running procedures, found and fixed issues in FLTBench runs, summarized mathematical proof-progress problems that appeared during the campaign, and evaluated the system to identify the next places that needed improvement.

## Contribution boundary

This is a collaborative project. The card records my system, tooling, experiment, and evaluation contributions while keeping the complete swarm implementation and other collaborators' work separate. ContextSwarmJudge is the associated judging and verification layer; its original implementation is recorded in its own collaborative card.

## What this establishes

The project provides an inspectable system-and-benchmark setting for asking how formal proof progress, tool feedback, and large-scale execution interact.

## What this does not establish

It does not establish that the full formalization of FLT was completed, that every part of the system was my individual work, or that the observed setup generalizes to mathematical research in general.

## What changed in my research direction

The campaign made a gap visible between a system producing many locally checkable actions and a later researcher being able to identify, trust, and continue the mathematical work those actions represented.

## Next question

Which proof objects, traces, links, and evidence conditions allow progress from a long formalization run to become reusable research state?

