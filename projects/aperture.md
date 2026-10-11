---
id: aperture
title: Aperture
theme: organization-and-replaceability
status: prototype
visibility: private
repository: https://github.com/yuan-chengzhi/aperture-worlds
last_reviewed: 2026-10-11
---

# Aperture

## Question

What does replaceable mean when dependencies, caches, formal environments, and running processes carry hidden state?

## What exists

Aperture studies replaceability in levels:

- L1: independent construction;
- L2: deployment;
- L3: migration;
- L4: mid-run switching.

A bounded Lean integration closes an upstream cache and resident-REPL path to isolate the mutable-dependency cache issue. The levels are kept separate because evidence at one level should not be promoted to another.

## My role

I contributed to experimental framing, issue diagnosis, and interpretation of the level-specific evidence.

## Evidence

Read the [repository](https://github.com/yuan-chengzhi/aperture-worlds) and the [audited foundation commit](https://github.com/yuan-chengzhi/aperture-worlds/commit/5e72b0b1859bee3ae71babbecf6eadd20c9061bc).

## What this establishes

Replaceability is a contract with levels and failure modes, not a binary property.

## What this does not establish

A bounded construction is not a complete replaceable research platform and is not a real-model cognitive experiment.

## What changed in my research direction

It turned agent replacement into a systems question about what state is carried across a boundary and what must be revalidated.

## Next question

Can migration and mid-run switching be tested without silently promoting evidence across replaceability levels?
