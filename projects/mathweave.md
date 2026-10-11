---
id: mathweave
title: MathWeave
theme: persistent-research-worlds
status: implemented
visibility: private
repository: https://github.com/yuan-chengzhi/MathWeave
last_reviewed: 2026-10-11
---

# MathWeave

## Question

What would a map-first platform for long-horizon mathematical research need to preserve, derive, and refuse to infer?

## What exists

MathWeave uses an append-only world ledger as the canonical source and derives a Mathematical Map, bounded navigation, retrieval, frontiers, and local dossiers from it. The executable v0.1 slice keeps exact versions and receipts visible. Retrieval locates material; only explicit admissions assert mathematics.

The implementation also forced architectural corrections: generic relations cannot be assumed to create closure obligations, and FORMALIZES does not automatically create a closure obligation.

## My role

I contributed to architecture review, implementation feedback, and the analysis of how the executable slice changed the original design assumptions.

## Evidence

See the [repository](https://github.com/yuan-chengzhi/MathWeave) and the audited [v0.1 commit](https://github.com/yuan-chengzhi/MathWeave/commit/393fca141df3aa990378edb53fa3cc9e89445011). The architecture notes at that snapshot document the ledger, admission, projection, and retrieval boundaries.

## What this establishes

A persistent research world can keep canonical admissions separate from derived views and bounded retrieval. This makes epistemic boundaries executable and inspectable.

## What this does not establish

A map, search result, relation, or retrieved document does not automatically constitute a mathematical admission or a scientific discovery.

## What changed in my research direction

The implementation fed back into the theory. Derived views lost canonical write authority, exact-version discipline became explicit, and more connected stopped meaning more true.

## Next question

Which admission and provenance contracts remain stable under adversarial, long-horizon use?
