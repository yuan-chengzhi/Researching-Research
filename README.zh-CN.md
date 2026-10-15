# Researching Research

**Chengzhi Yuan · 多智能体系统 · AI for Mathematics**  
[English](README.md) · [研究历程](research-development.zh-CN.md) · [研究图谱](docs/research-graph.zh-CN.md) · [当前问题](current-questions.md)

我关注 Agent Swarm 的群体行为、组织方式与能力扩展。我喜欢构建工具、架构和共享环境，推测它们怎样影响 Agent 的行动，再用实际运行检验——偏离预期的行为常常是新问题的起点。形式化数学，特别是长程证明，是我目前探索这些问题的主要场景。

**怎样让许多 Agent 的局部探索形成持续推进的整体？系统又能否从运行中自主发现、实施、检验并积累有效改进，甚至改变自己寻找与评价改动的方法？**

这是持续演化的个人研究地图，不是一个已经完成的统一系统。它既记录已有成果，也记录没有达到目标的实验、尚未完成的探索和改变问题理解的经历。

> **阅读与访问：** 下面先链接本仓库内的项目说明。多数原始代码、运行数据和团队稿件仍为私有或内部材料；固定版本链接不等于公开可访问。见[材料访问与分享说明](docs/access-and-sharing.md)。

## 从实际工作开始

| 工作 | 我的主要贡献 | 产出与状态 |
| --- | --- | --- |
| [Putnam 2025：证明闭环与 Lean 工具](projects/putnam-2025.md) | 实验平台、提示词、工具开发、运行排查与结果分析 | 12 题均达到内部 `final_verified`；题内八次并行，逐题记录用时合计约 5.5 小时。固定报告已链接，非官方竞赛成绩。 |
| [ContextSwarm：FLT 证明进展与系统迭代](projects/contextswarm.md) | 对照上层证明检查局部成果；诊断父路线查询缺口；参与提示词与资料读取改进 | 团队系统、十项任务的 FLTBench 与 ICLR 2027 投稿；整体 FLT 形式化尚未完成。 |
| [同一 FLT 项目的协作证据分析](projects/flt-proof-weaving-aamas.md) | 按证明对象、版本和事件时状态重建过程；案例、个人诊断文档、部分可视化与稿件修订 | AAMAS 2027 投稿；团队累计约 100B tokens、40,000 aggregate agent-hours，不是另一项独立系统成果。 |

两条较早或并行的探索补充了这条主线：[《集体加速》](projects/collective-acceleration.md)从随机过程与网络关系研究进度共享；[TacticWorld](projects/tacticworld.md)提出从同状态多个 tactic 的结构化后果中学习，完整训练与评估尚未完成。两者的研究阶段和证据类型在项目卡中分别说明。

## 实践怎样改变了问题

Putnam 中，无附加自然语言优先提示的 Agent 也会自行先推理、再写 Lean。这让我开始区分**提供必要的工作能力**与**规定工作顺序**，而不是默认流程越细越好。

在 FLT 项目中，一个子目标明明已有上层用途，Agent 却可能因查询接口缺失而无法获得它；共享信息被定位为“经验库”时，设计也容易围绕记录、检索和复用展开，忽略未成熟想法、求助与候选路线。随后对运行轨迹的分析进一步要求我区分：对象存在、信息送达、实际使用和整体推进，分别需要什么证据。

这些经历把问题从“怎样设计更好的环境”推向“系统能否识别并突破既有设计的局限”。更详细的过程见[研究历程](research-development.zh-CN.md)；具体诊断和证据边界留在对应项目卡中。

## 正在探索的方向

形式化证明为协作提供可表达的目标、依赖与验证反馈，但不会自动给出最合适的组织方式。我希望结合系统实验与数学建模，研究系统级自主探索和持续演化：既研究如何发现、试验并保留有效改动，也研究求解与改进如何分配资源、不同演化方向如何共存，以及改进何时真正扩展群体能力。

共享记忆、工具接口和研究状态是可能的切入点，**不是对整个研究对象的预先限定**。目前尚未得到系统级自主演化有效性的结论。见[未来研究方向](docs/research-plan.zh-CN.md)与[当前问题](current-questions.md)。

## 工具、原型与完整索引

[Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md)和 [pi-lean-tools](projects/pi-lean-tools.md)是 Putnam 实验相关工具，不重复计算为独立结果。Metron、Persistent Mathematical Worlds、MathWeave、PMW Research Platform、Aperture 等继续探索状态、持久化和组织边界，详见[研究图谱](docs/research-graph.zh-CN.md)。[oncewhere](projects/oncewhere.md)保留为相邻创作，不包装成数学系统组件。

<details>
<summary>展开完整索引：研究项目、工具、阶段产出与关联参考</summary>

条目数不等于独立项目或论文数。状态与来源可见性按各条目的最近核对记录展示；证据与个人贡献详见项目卡。`ContextSwarmJudge` 仅为关联参考，不是我的仓库贡献。

<!-- project-index:start -->
| 条目 | 状态 | 我的角色 | 原始来源 |
| --- | --- | --- | --- |
| [Collective Acceleration](projects/collective-acceleration.md) | 分析 | 个人工作 | 内部材料 |
| [Putnam 2025: formal proof experiments](projects/putnam-2025.md) | 已有实验记录 | 个人工作 | 私有来源 |
| [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) | 已有实验记录 | 个人工作 | 私有来源 |
| [Pi Lean Tools](projects/pi-lean-tools.md) | 原型 | 个人工作 | 私有来源 |
| [ContextSwarm](projects/contextswarm.md) | 合作研究 | 团队中的贡献 | 私有来源 |
| [ContextSwarmJudge](projects/contextswarm-judge.md) | 关联组件 | 关联参考；无该仓库贡献 | 私有来源 |
| [ICLR 2027 stage output: FLT system and FLTBench](projects/flt-iclr-stage-output.md) | 已投稿 | 团队中的贡献 | 内部材料 |
| [FLT campaign: collaboration analysis (AAMAS 2027)](projects/flt-proof-weaving-aamas.md) | 已投稿 | 团队中的贡献 | 内部材料 |
| [Metron](projects/metron.md) | 原型 | 个人工作 | 私有来源 |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md) | 原型 | 个人工作 | 私有来源 |
| [MathWeave](projects/mathweave.md) | 已有实现 | 个人工作 | 私有来源 |
| [PMW Research Platform](projects/pmw-research-platform.md) | 原型 | 个人工作 | 私有来源 |
| [Rights in the Exponent](projects/rights-in-the-exponent.md) | 分析 | 个人工作 | 私有来源 |
| [Aperture](projects/aperture.md) | 原型 | 个人工作 | 私有来源 |
| [Agent Math Frontier](projects/agent-math-frontier.md) | 已有实现 | 个人工作 | 公开来源 |
| [oncewhere](projects/oncewhere.md) | 相邻创作 | 个人工作 | 私有来源 |
| [Trace analysis](projects/trace-analysis.md) | 研究线索 | 个人工作 | 内部材料 |
| [TacticWorld](projects/tacticworld.md) | 研究设计 | 个人工作 | 私有来源 |
<!-- project-index:end -->

</details>

## 如何继续维护

新增材料时，先写清问题、实际工作、最强证据与结果边界，再更新项目卡和 `project-index.json`；新问题同步到 `current-questions.md` 与 `question-index.json`。不要为了保持一条整齐路线而改写历史。

```bash
python scripts/build_index.py --write
python scripts/build_index.py --check
python -m unittest discover -s tests -v
```

[项目卡模板](docs/project-card-template.md) · [证据与状态约定](docs/evidence-and-status.md) · [路线修订记录](decisions/0003-scope-contribution-and-reader-path.md)
