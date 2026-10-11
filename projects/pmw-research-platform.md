---
id: pmw-research-platform
title: PMW Research Platform
theme: organization-and-replaceability
status: prototype
visibility: private
repository: https://github.com/yuan-chengzhi/pmw-research-platform
last_reviewed: 2026-10-11
---

# PMW Research Platform

## Question

What is the smallest runtime boundary that lets replaceable research sessions operate over a persistent world?

## What exists

The platform is a production-candidate cohort and runtime control plane. It coordinates shared input, concurrency, lifecycle, and settlement while keeping persistent mathematical state separate from replaceable research sessions.

The current system is not yet a full live multi-agent research plane: agents in one cohort cannot yet query peers in real time, call a verifier, or coordinate a mathematical route through the runtime.

## My role

I worked on the platform's research framing and the analysis of the boundary between lifecycle control and mathematical coordination.

## Evidence

Read the [repository](https://github.com/yuan-chengzhi/pmw-research-platform) and the audited [commit d28748c](https://github.com/yuan-chengzhi/pmw-research-platform/commit/d28748c8a8a67d19b17ccbd347b8c5a853c33782).

## What this establishes

Cohort and runtime lifecycle can be treated as a distinct control-plane problem around a persistent research world.

## What this does not establish

The present platform is not evidence that agents already share cognition or coordinate a complete mathematical route in real time.

## What changed in my research direction

It separated the social and runtime organisation of research from the semantics of the mathematical world. That separation makes later claims easier to audit.

## Next question

What is the smallest authenticated interface through which agents can coordinate a mathematical route without giving the runtime hidden semantic authority?
