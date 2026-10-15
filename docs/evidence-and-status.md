# Evidence, status, and contribution

[Access and sharing](access-and-sharing.md) · [Card template](project-card-template.md)

This atlas separates what exists, what I did, what was observed, and what remains an interpretation. A fixed source is not automatically public, independently audited, or sufficient for every claim on its card.

## Personal role is independent of maturity

| `ownership` | Meaning |
| --- | --- |
| `direct` | Work carried out directly by me, including work with AI coding assistance. Not a claim that every dependency or line was authored unaided. |
| `collaborative` | A contribution to a team project. Requires `role_scope`, `contribution_scope`, and `not_my_contribution`. |
| `reference` | An associated component or evidence source, not my repository contribution. Requires `reference-only` status, explicit reference role, and empty `contribution_scope`. |

ContextSwarmJudge is reference-only. Analysis of its outputs belongs under the FLT/AAMAS contribution; an experiment-local patch described in the Putnam report does not establish contribution to the team repository.

A tool, an experiment using it, and a paper analyzing that experiment are related entries, not automatically three independent projects. ICLR and AAMAS describe distinct outputs of the same FLT campaign.

## Status describes the kind of work

| Status | Meaning |
| --- | --- |
| `design` | A question, protocol, or architecture is specified; its proposed result is not established. |
| `prototype` | An apparatus exists but its scope or contract is still changing. |
| `implemented` | The described mechanism is inspectable; scientific effectiveness is not implied. |
| `experimentally-observed` | A stated run or observation is recorded; control quality, replication, and interpretation must be read separately. |
| `collaborative-research` | An ongoing or recorded team research project; personal role is specified independently. |
| `submitted` | Submission is reported; acceptance or scientific validity is not implied. |
| `analysis` | A bounded model, comparison, or interpretation. |
| `research-thread` | A working line of inquiry rather than a standalone completed project. |
| `adjacent-work` | Creative or other work outside the mathematical-agent system. |
| `reference-only` | An associated component with no personal repository contribution claimed. |
| `archived` | Retained for history rather than an active direction. |

## Evidence and provenance

Idea, design, implementation, test, recorded experiment, formal proof, and independent replication are different evidence types, not a maturity ladder. A formal check is relative to a statement, assumptions, and checker; it does not by itself establish intended meaning, usefulness, or collective benefit.

| `evidence_status` | Meaning |
| --- | --- |
| `fixed-commit` | At least one cited artifact has a full immutable GitHub commit identifier; this is an addressability label, not an audit of every claim. |
| `branch-pinned` | A named branch and path identify current context; the content can move. |
| `branch-unpinned` | A moving branch still needs a historical reference. |
| `internal-artifact` | Internal material is described but no stable externally accessible artifact is supplied here. |
| `internal-thread` | A working analysis thread without a standalone repository. |
| `author-report` | An author account is available, but the primary artifact is not supplied or audited through this atlas. |

Source visibility (`public`, `private`, `internal`) is separate from evidence strength. Review dates indicate the last review of that entry's wording and identified sources, not a rerun of its experiments. Unchanged entries retain their older dates; updates must say when individual claims come only from an author account.

## Bounded claims

Use `[implemented]`, `[observed]`, `[computed]`, `[proven]`, `[open]`, or `[unverified]` only with the appropriate artifact and scope. A report of proof verification is not a new independent verification by this atlas. An object's presence does not establish delivery, use, or causal benefit. The Putnam internal `final_verified` result is not an official contest score; summed problem runtimes are not the full elapsed investigation or aggregate agent-hours.

Each important claim should identify its supporting artifact, exact scope, personal role, and tempting stronger inference that is not supported. If evidence is missing, say so rather than filling the gap with an unrelated repository snapshot.

## Evolution and maintenance

`relations` records why entries connect; `changed_by` records an observation or artifact that changed an interpretation. Neither field turns relevance into authorship or establishes causation. Keep stable IDs and historical decisions when a research direction changes. The generator validates metadata and keeps tables synchronized; it does not validate scientific conclusions or remote access permissions.
