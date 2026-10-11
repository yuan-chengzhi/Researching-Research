# Project card template

Copy this file to projects/<stable-id>.md. Keep the id stable after the card is introduced.

Use the index for mechanical fields and use the prose sections for research judgment. A card is allowed to say that the strongest result is negative, partial, or still unverified. The index also records evidence_status, relations, and changed_by so that later additions can be audited as part of the route.

Front matter should include: id, title, theme, status, visibility, repository, and last_reviewed.

## Question

What question does this project make concrete?

## What exists

Name the implementation, experiment, document, or artifact that can be inspected.

## My role

State the work I personally did. Separate it from the work present in the repository.

## Evidence

Link to current materials and, for important claims, fixed commit or tag URLs.

## What this establishes

Use a bounded claim. Say what the evidence supports.

## What this does not establish

State the tempting stronger conclusion that the evidence does not support.

## What changed in my research direction

Explain whether this project narrowed, redirected, or strengthened the central question.

## Next question

Name the next experiment or design question that could change the interpretation.


## Machine-readable evolution fields

In project-index.json, add:

- evidence_status: fixed-commit, branch-pinned, branch-unpinned, or internal-thread;
- relations: typed links to other project IDs, with a one-sentence reason;
- changed_by: the evidence artifact and the interpretation it changed.

These fields describe how the map evolves. They do not replace the prose sections or turn the research arc into a forced chronology.
