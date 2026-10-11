# Evidence and status contract

This repository records a research trajectory. Its vocabulary is meant to keep implementation, observation, and interpretation separate.

## Status describes the kind of work

| Status | Meaning |
| --- | --- |
| design | The main result is a proposed architecture, protocol, or question. |
| prototype | A working apparatus exists, but its contract or scope is still changing. |
| implemented | The described mechanism is present and inspectable. This says nothing by itself about scientific effectiveness. |
| experimentally-observed | A controlled run or reproducible observation exists. |
| submitted | A manuscript or stage output has been submitted; this does not imply acceptance or scientific validity. |
| analysis | The main contribution is a theory, comparison, or interpretation whose validation remains bounded. |
| adjacent-work | The project belongs to the wider personal trajectory but is not a component of the mathematical-agent system. |
| research-thread | The work is currently an analysis thread rather than a standalone repository. |
| archived | The project is preserved for historical context and is no longer an active direction. |

## Evidence levels

A project may contain several evidence levels at once:

- idea — a question or hypothesis;
- design — a stated architecture or protocol;
- implementation — code or an executable artifact;
- test — a check that the apparatus behaves as intended;
- experiment — a controlled observation with preserved inputs and outputs;
- formal proof — a result accepted by the relevant formal system;
- external validation — evidence from an independent audience, reviewer, or replication.

Evidence levels are not a ladder. A design can be conceptually important before implementation; an implementation can remain scientifically unvalidated.

## Claim labels

Use bounded labels when a card discusses a result:

- [implemented] — the mechanism exists in the cited artifact;
- [observed] — the behaviour occurred in a stated run;
- [proven] — the formal system accepted the claim;
- [computed] — a number was produced by a specified computation;
- [open] — the claim remains unresolved;
- [unverified] — the claim is currently a hypothesis or interpretation.

Never infer a stronger label from a weaker one. Code presence does not imply scientific effectiveness, and a retrieval result does not imply mathematical admission.

## Live links and fixed evidence

Each card may use both:

- a live link to the current branch or repository, for continuing work;
- a fixed link to a commit or tag, for auditing the wording that supports a historical claim.

The live link is expected to move. The fixed link should not. When a new result changes a claim, update the card and add a decision record if the research arc itself changes.

## Review rules

Before adding a claim to a card, ask:

1. What exact artifact supports it?
2. Is the artifact current or pinned?
3. What did I personally do?
4. What stronger statement might a reader incorrectly infer?
5. What next observation could prove this wording wrong?


## Evidence status and evolution links

The index records whether a citation is auditable at the current snapshot:

| evidence_status | Meaning |
| --- | --- |
| fixed-commit | The strongest cited artifact is pinned to a full commit SHA. |
| branch-pinned | The cited artifact is pinned to a named branch and path; use it for current context, not immutable history. |
| branch-unpinned | The card currently points at a moving branch and its historical claim must remain provisional. |
| internal-thread | The evidence is a working analysis thread without a standalone repository. |

Each project also has typed relations and changed_by entries. Relations describe why two projects are connected; changed_by records which artifact changed the next interpretation. The map can therefore grow by adding a card without rewriting the old cards, while still preserving the edges that matter.
