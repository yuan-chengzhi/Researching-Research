# Current questions

Last reviewed: 2026-10-11

Machine-readable question registry: [question-index.json](question-index.json)

Q0 is the current frontier hypothesis. Q1–Q5 are the component questions exposed by earlier experiments; Q6 remains an adjacent personal question. The question registry stores short summaries and typed links; this document remains the prose source of truth.

<a id="q0"></a>\n## Q0 — Can the research substrate itself evolve?

Status: hypothesis

With the model, budget, Lean toolchain, verifier, provenance boundary, and holdout tasks fixed, can controlled experiments on training-task traces select substrate choices that transfer to unseen tasks without increasing stale or invalid inheritance?

Evidence to seek next: a small four-arm experiment with a replayable event schema, one mutation family, and a sealed holdout.

These are live questions, not a checklist of promises. A new repository belongs in the atlas when it changes one of them or opens a genuinely new direction.

<a id="q1"></a>\n## Q1 — What makes a local feedback loop trustworthy?

Status: active

Can a mathematical agent inspect the exact local state produced by an action, test the relevant consequence, and preserve the result as evidence about that action? This includes proof-state tools, Lean-aware probes, prompt design, and experiment protocols.

Evidence to seek next: fixed comparisons between feedback modes, with the protocol and failure cases preserved.

<a id="q2"></a>\n## Q2 — How should unfinished mathematical work be represented?

Status: active

Which distinctions matter for continuation: active routes, valid certificates, unresolved obligations, failed branches, or the provenance of a claim? What should remain machine-readable without pretending to be a universal progress score?

Evidence to seek next: small tasks where two representations lead to different continuation decisions.

<a id="q3"></a>\n## Q3 — When does persistent state become inherited research rather than a larger context window?

Status: active

A later agent should be able to inherit a state, understand what is provisional, and make a new contribution without silently treating retrieval as proof. The test must separate causal inheritance from mere access to more text.

Evidence to seek next: versioned handoffs with explicit admissions, provenance, and adversarial checks.

<a id="q4"></a>\n## Q4 — What does replaceability require?

Status: active

Can an agent, maintainer, verifier, or runtime component be replaced at a stated semantic-contract level without invalidating the evidence? Which interfaces are meaningful contracts, and which are only implementation conveniences?

Evidence to seek next: level-specific migration and mid-run switching experiments.

<a id="q5"></a>\n## Q5 — How can a research system learn from failures without flattening evidence?

Status: open

A research system should make relationships visible while preserving the differences between code, tests, computed results, formal proof, and open conjecture. How should it record a failed experiment that changes the research direction?

Evidence to seek next: decision records that connect a negative result to a revised question.

<a id="q6"></a>\n## Q6 — What should remain after a shared experience ends?

Status: adjacent

This question belongs to oncewhere. It is not a hidden technical requirement for the mathematical-agent system, but it is part of the same personal interest in persistence, return, and what a system chooses to preserve.
