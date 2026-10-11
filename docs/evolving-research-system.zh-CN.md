# 可演化的形式化数学研究 substrate

> 状态：研究假说与实验议程。这份文档描述的不是一个已经完成的系统。

## 研究范围

我目前不把模型参数演化作为第一个研究对象，也不把更好的单 agent harness 当作最终问题。它们可以作为控制变量或提供能力的机制。我的研究单位是做形式化数学的一群 agent 周围的 research substrate：保存什么、如何连接、什么可以被继承，以及下一个挑战如何被选择。

需要区分的是：一个 proof 通过 verifier，和一份研究工作能够被另一个 agent 安全地继续，不是同一件事。后者需要形式化 artifact、过程证据、provenance、负面结果和明确的 admission 边界。

## 三个耦合部分

### Proof-world substrate

agent 在 Lean 环境中提出或修改形式化 artifact。substrate 保存 statement、definition、goal、subgoal、candidate lemma、certificate、未解决义务、脚本、代码、工具观察、诊断、attempt、handoff 和版本。

### Research-system evolution

训练 trace 和 verdict 可以用来提出并比较 object schema、link、admission 规则、retrieval 视图、context packaging、工具、routing、handoff 和 agent organization 的变化。每个提案都是有版本的 mutation，带有 diff、理由、可 replay 的评估和回滚点。不能因为训练分数提高，就自动把 mutation 升格。

### Challenge frontier

失败和瓶颈可以推动生成更长依赖、更难复用或更高协作要求的形式化任务。训练侧的 curriculum 可以变化；holdout 集必须在评估之前保持封存。

## 一个候选形式化

在某个时刻，可以把 substrate 写成 E_t = (O_t, L_t, P_t, G_t, V_t)：

- O_t：类型化的数学对象、过程对象和系统对象；
- L_t：带证据和 admission 条件的类型化 link；
- P_t：agent 和工具的交互协议；
- G_t：任务和 curriculum 的生成器；
- V_t：诊断、评估和验证接口。

每次运行产生 append-only event log。每条事件都带有 artifact identity、精确版本、agent 或工具、目标、操作、反馈、admission 状态和 evaluator 版本。retrieval exposure 必须和数学有效性分开记录。

## 稳定内核与可演化层

在演化开始前，应该固定这些边界：

- 可信的 Lean 检查和明确的形式陈述边界；
- 不可变的 artifact identity 和版本 lineage；
- provenance 与可 replay 的 event log；
- candidate、checked、accepted、rejected、stale 等明确状态；
- 冻结的 holdout harness 与 contamination 边界；
- 不能把训练成功自动升格为科学结论。

这些部分则可以作为受控演化的候选：

- object schema 的增删；
- semantic、structural、epistemic、operational、provenance 和 retrieval link；
- admission 与 staleness 策略；
- context compiler 与 retrieval exposure；
- handoff、compaction 和 routing；
- agent population 与任务 curriculum。

目标不是冻结一套想象中的人类组织，而是在固定 authority 和审计边界的同时，让组织假说可以被比较。

## 最小实验

先只研究一种 mutation，例如 typed-state admission 或 retrieval exposure。固定模型、Lean snapshot、任务预算、verifier 和 agent protocol，比较：

1. 没有持久状态；
2. 普通文本共享；
3. 固定的 typed provenance substrate；
4. 在训练任务上演化 schema 或 admission policy 的 substrate。

评估单位应是 research episode，而不只是孤立 proof attempt：中断、替换 agent 的继续、未解决义务的减少，以及在不相同任务上的 artifact reuse。记录 valid proof rate、获得 certificate 的时间、修复成本、重复工作、accepted artifact reuse、stale inheritance、admission 错误、token 与 Lean 成本、schema churn、回滚，以及对 holdout 任务的迁移。

可信的结果必须是在 holdout 上得到提升，同时没有显著增加陈旧或无效继承。只有训练集提升，在迁移发生之前都应视为 overfitting。

## 什么会推翻这个议程

如果更丰富的状态从未改善 continuation，如果演化只学到了 benchmark 特定捷径，如果 provenance 的成本压过了复用收益，或者协议变化无法 replay 和比较，就应该修改这个议程。负结果仍然有价值，因为它会定位 substrate 设计真正有用的边界。