# Current questions

Last reviewed: 2026-10-14

[中文方向说明](docs/research-plan.zh-CN.md) · [Machine-readable registry](question-index.json)

Q0 is the broad future direction; Q1–Q5 and Q7 are interacting research questions, Q8 concerns the organization of evolution itself, and Q6 remains an adjacent creative question. They are not a mandatory pipeline or a list of achieved capabilities.

<a id="q0"></a>
## Q0 — Can an Agent Swarm autonomously discover and sustain effective system changes?

Status: hypothesis

Can agents discover design opportunities, propose, implement, test, and retain improvements, and improve how they search and evaluate changes while preserving reliable task evaluation?

Modifiability is only the starting point. The system must identify worthwhile opportunities, implement and test changes, retain useful results, and potentially revise its own proposal and evaluation procedures. Shared memory and tool interfaces are candidate objects, not the whole scope. See the [future direction](docs/research-plan.md).

Evidence to seek: repeated gains on subsequent independent tasks under stated total budgets, with reliable evaluation and costs of discovery, testing, and maintenance included. A bounded first comparison is useful; one mandatory mutation family or fixed four-arm design is not yet a commitment.

<a id="q1"></a>
## Q1 — What makes a local feedback loop trustworthy?

Status: active

Can a mathematical agent inspect the exact local state produced by an action, test the relevant consequence, and preserve the result as evidence about that action?

This includes Lean probes, prompt choices, failure recovery, and action-effect signals. The Putnam A5 comparison motivates separating working capabilities from prescribed order; it does not establish a universally superior workflow. TacticWorld proposes a learning comparison, not a completed training result.

Evidence to seek: pinned comparisons between feedback modes, with settings, failures, and downstream actions preserved.

<a id="q2"></a>
## Q2 — How should unfinished mathematical work be represented?

Status: active

Which distinctions matter for continuation: active routes, valid certificates, unresolved obligations, failed branches, or the provenance of a claim?

Active routes, provisional claims, verified results, and missing conditions may require different representations. A stored relationship is not automatically a proof dependency or an actually used result.

Evidence to seek: controlled tasks where representations change continuation decisions, with the dependencies and versions available at the time retained.

<a id="q3"></a>
## Q3 — When does persistent state become inherited research rather than a larger context window?

Status: active

Can a later agent inherit a versioned state, understand what is provisional, and make a new contribution without silently treating retrieval as proof?

Access, delivery, use, and benefit are different events. A later agent should recognize provisional material rather than silently promote retrieval into proof.

Evidence to seek: versioned handoffs and matched comparisons that distinguish inherited work from simply receiving more text.

<a id="q4"></a>
## Q4 — What does replaceability require?

Status: active

Can an agent, maintainer, verifier, or runtime component be replaced at a stated semantic-contract level without invalidating the evidence?

Replacement can concern state, tools, agents, or organizational roles. The semantic contract being preserved must be explicit; replaceability is not one binary property.

Evidence to seek: level-specific migration or mid-run switching tests, including failures at mutable dependencies.

<a id="q5"></a>
## Q5 — How can a research system learn from failures without flattening evidence?

Status: open

How should a research system record failures that change its direction while preserving differences between code, tests, computed results, formal proof, and open conjecture?

An observed recurrence is not by itself evidence that feedback was received and ignored. Evidence about implementation, local verification, use, and causal benefit must remain distinguishable.

Evidence to seek: event-time reconstruction, records of actual use, and interventions that discriminate competing explanations.

<a id="q6"></a>
## Q6 — What should remain after a shared experience ends?

Status: adjacent

What can remain returnable, interpretable, and alive after an immediate shared experience ends?

This is the adjacent question explored by [oncewhere](projects/oncewhere.md). It is a personal and thematic connection, not a hidden technical requirement or validation of the mathematical-agent system.

<a id="q7"></a>
## Q7 — How does local work become collective progress?

Status: active

How do network relations, task dependencies, shared information, and organizational choices let local work contribute to a common goal?

Task structure can help organize work without fully specifying the organization. Network-based models, proof dependencies, and shared research objects offer complementary ways to study this. Resetting an attempt need not erase its external records.

Evidence to seek: explicit assumptions in mathematical models and experiments distinguishing local activity from useful contributions to a shared goal.

<a id="q8"></a>
## Q8 — How should task work and system evolution share resources and preserve diversity?

Status: open

How should task-solving and system-improvement teams share context and compute, and when can multiple competing design directions prevent premature convergence?

An agent improving the system spends resources it cannot simultaneously spend on the task. Separate teams may reduce that conflict but introduce communication and evaluation costs. A single successful design lineage may also eliminate useful alternatives too early.

Evidence to seek: budget-accounted comparisons of coupled and separated roles, together with measures of retained search diversity and performance after task changes. These mechanisms are proposed questions, not established results.
