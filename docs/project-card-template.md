# Project card template

Use a stable `projects/<id>.md` path and record the same ID and metadata in `project-index.json`. A partial or negative result is acceptable; the description must make its evidence clear.

Front matter: `id`, `title`, `theme`, `status`, `visibility`, `ownership`, `repository`, `last_reviewed`. Use `direct`, `collaborative`, or `reference` independently of project maturity; see [the evidence contract](evidence-and-status.md).

## Question

What question did the work actually address, rather than a later agenda retrospectively assigned to it?

## What exists and my role

Name the artifact and specific personal actions. Separate a team's system, benchmark, paper, or run budget from individual contributions. Distinguish implementation, proposed design, observed result, and unfinished evaluation.

## Representative case

When useful, describe an observed problem, the diagnosis or design choice, the action taken, and what changed. Do not describe an untested improvement as an established effect.

## Evidence

Provide the smallest relevant source and a fixed commit for historical claims where available. State access restrictions and which claims rely on an author account rather than inspected primary material. A repository root or code snapshot does not automatically prove a particular contribution, run, or acceptance test.

## Result boundary and next question

State what the evidence does not establish and how the observation changed the question. Do not force parallel explorations into a strict chronology.

## Index maintenance

`evidence_status`, `relations`, and `changed_by` must agree with the card. Collaborative entries need explicit contribution boundaries. Reference-only entries must have empty `contribution_scope`, `role_scope: reference-only-no-repository-contribution`, and no achievement claim. After updates, run the generator, check mode, and tests documented in the README.
