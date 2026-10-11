---
id: trace-analysis
title: Trace analysis
theme: evidence-and-diagnosis
status: research-thread
visibility: internal
repository: internal:trace-analysis
last_reviewed: 2026-10-11
---

# Trace analysis

## Question

How can a failure trace become a research result without being over-interpreted?

## What exists

This is currently an internal analysis thread around swarm traces, FLT-related experiments, as-of replay, and the boundary between evidence and diagnosis. It asks which trace fields are sufficient to reconstruct what happened, compare branches, and explain why a result should change the next question.

## My role

My contribution is the analysis itself: inspecting traces, separating implementation failures from research failures, and turning negative evidence into more precise questions.

## Evidence

The thread is represented here until the apparatus becomes a standalone repository. It should not be cited as a complete causal methodology.

## What this establishes

A trace can be valuable even when it does not produce a positive mathematical result: it can reveal a missing contract, an untestable assumption, or a misleading metric.

## What this does not establish

Trace analysis alone does not provide a universal causal explanation of swarm outcomes.

## What changed in my research direction

It made failure interpretation a first-class part of the research route rather than an afterthought to successful runs.

## Next question

Which trace fields and replay boundaries are sufficient for an independent diagnosis?
