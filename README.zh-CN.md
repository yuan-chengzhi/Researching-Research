# Researching Research

## 我的 AI×数学研究历程

这是一个记录我如何从 Putnam 2025 和局部形式化证明实验，逐步走向“可演化研究 substrate”问题的活地图。

我不是先决定要做一个大规模 agent swarm。我先追问一个更小的问题：如果给 agent 一个足够好的形式化数学环境，它的数学能力能否变成可靠的工作？Pi Math First Proof Swarm、Ralph loop 和 Pi Lean Tools 通过反复行动、Lean 工具、局部验证和反馈来探索这个问题。

随着工作进入多 agent 场景，“环境”的含义也扩大了：共享状态、proof object、未完成路线、provenance、handoff 和 admission。现在的问题进一步变成：这些对象和协议能否由实验数据推动改变，同时保持形式验证边界和冻结的测试评估？

始终不变的兴趣不是预先写好一套 workflow，而是构造能够让 agent 发挥、保存并继续使用数学能力的环境。这个仓库记录问题如何改变，也记录促成改变的限制和负面证据。

## 为什么首先研究形式化数学

形式化证明适合作为第一个实验场，因为 Lean 可以相对于明确的形式陈述检查 proof，文件、工具调用、诊断和版本也可以 replay。它没有解决 statement fidelity、定义选择、库访问、解释和数学价值；这些边界本身就是研究问题。

## 如何阅读

1. 先看[研究发展历程](research-development.zh-CN.md)，理解问题如何逐步形成。
2. 再看[当前研究路线](research-arc.md)和[当前问题](current-questions.md)，区分历史与现在的问题空间。
3. 打开项目卡，分别阅读问题、证据、我的作用和结果边界。
4. 需要复核历史事实时，优先使用固定 commit 链接。
5. 比较不同项目之前，先读[证据与状态约定](docs/evidence-and-status.md)。

## 研究地图

| 主题 | 问题 | 代表项目 |
| --- | --- | --- |
| 可靠行动与反馈 | agent 能否完成一次数学行动，并获得可信的局部反馈？ | [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md)、[Pi Lean Tools](projects/pi-lean-tools.md) |
| 未完成的数学工作 | 活跃尝试、有效证书和未解决义务应该如何共存？ | [Metron](projects/metron.md) |
| 持久研究世界 | 研究状态能否在 agent 和会话被替换后继续存在，同时不把临时材料冒充为真理？ | [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md)、[MathWeave](projects/mathweave.md) |
| 组织与可替换性 | 一个研究组织实际控制什么？替换究竟意味着什么？ | [PMW Research Platform](projects/pmw-research-platform.md)、[Aperture](projects/aperture.md)、[Rights in the Exponent](projects/rights-in-the-exponent.md) |
| 证据与诊断 | 如何解释一个 swarm 的结果，而不是把证据压缩成一个分数？ | [Agent Math Frontier](projects/agent-math-frontier.md)、[Trace analysis](projects/trace-analysis.md) |
| 相邻创作 | 如何把共同经历保存成可以再次进入的东西？ | [oncewhere](projects/oncewhere.md) |

## 精选项目

<!-- project-index:start -->
| 项目 | 主题 | 状态 | 可见性 | 证据 |
| --- | --- | --- | --- | --- |
| [Pi Math First Proof Swarm](projects/pi-math-first-proof-swarm.md) | reliable-action-and-feedback | experimentally-observed | private | branch experiment/e13; fixed commit to be pinned after branch audit |
| [Pi Lean Tools](projects/pi-lean-tools.md) | reliable-action-and-feedback | prototype | private | branch codex/frontier-probe-command; fixed commit to be pinned after branch audit |
| [Metron](projects/metron.md) | unfinished-mathematical-work | prototype | private | branch metron/f0-runtime-v2; fixed commit to be pinned after branch audit |
| [ContextSwarm / FLT analysis](projects/contextswarm-flt-analysis.md) | evidence-and-diagnosis | analysis | internal | https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/commit/88a591986900a204a1b1acd757740354ed6f25bc; https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/commit/82307d2a1d553d3493a56fe7a936ffc2e3dd4fbf |
| [Persistent Mathematical Worlds](projects/persistent-mathematical-worlds.md) | persistent-research-worlds | prototype | private | https://github.com/yuan-chengzhi/persistent-mathematical-worlds/blob/codex/c07-apparatus-fix/docs/decisions/0004-polycentric-agenda-direction.md |
| [MathWeave](projects/mathweave.md) | persistent-research-worlds | implemented | private | https://github.com/yuan-chengzhi/MathWeave/commit/393fca141df3aa990378edb53fa3cc9e89445011 |
| [PMW Research Platform](projects/pmw-research-platform.md) | organization-and-replaceability | prototype | private | https://github.com/yuan-chengzhi/pmw-research-platform/commit/d28748c8a8a67d19b17ccbd347b8c5a853c33782 |
| [Rights in the Exponent](projects/rights-in-the-exponent.md) | organization-and-replaceability | analysis | private | https://github.com/yuan-chengzhi/rights-in-the-exponent/commit/2b7291c564d609a68d580f5279af4c3c8ee27136 |
| [Aperture](projects/aperture.md) | organization-and-replaceability | prototype | private | https://github.com/yuan-chengzhi/aperture-worlds/commit/5e72b0b1859bee3ae71babbecf6eadd20c9061bc |
| [Agent Math Frontier](projects/agent-math-frontier.md) | evidence-and-diagnosis | implemented | public | https://github.com/yuan-chengzhi/agent-math-frontier/commit/e5fb06928f26e0762e62c17b2cea241c29c40918 |
| [oncewhere](projects/oncewhere.md) | adjacent-creative-work | adjacent-work | private | https://github.com/yuan-chengzhi/oncewhere/commit/9ea4c02316cdd96ca5c4f8f6d7a0af2bdcfe2402 |
| [Trace analysis](projects/trace-analysis.md) | evidence-and-diagnosis | research-thread | internal | analysis thread; repository link will be added if the apparatus becomes a standalone project |
<!-- project-index:end -->

## 我的工作

项目卡会把“仓库里存在什么”和“我的具体贡献”分开。到目前为止，我在数学 agent 项目中的工作包括：设计 prompt 和实验协议，改进 proof-state 处理与局部反馈循环，分析实验 trace、失败原因和 branch 行为，修复问题，提高可复现性，以及完成数据分析、图表、校对和修改。

## 这个地图如何演化

以后加入新 repo 时，只需要完成一组小而可复核的改动：

1. 在 projects/<id>.md 创建稳定的项目卡。
2. 在 project-index.json 增加一条记录。
3. 尽可能把最强证据固定到 commit 或 tag。
4. 写清楚证据建立了什么，以及没有建立什么。
5. 运行 python scripts/build_index.py --write 刷新机械索引。
6. 只有当新项目改变了正在追问的问题时，才更新 current-questions.md。
7. 只有当研究路线的解释发生重大改变时，才新增 decision record。

脚本和 workflow 都保持很小：它们检查结构并维护索引，不替你生成研究意义、个人贡献或超出证据范围的结论。

## 这个仓库不声称什么

- 它没有把所有项目包装成一个已经完成的自主数学研究系统。
- 它不把“已经实现”当成“已经证明科学有效”。
- 它不为所有形式的未完成工作强行使用一个进度分数。
- 它不把共享状态等同于共享认知。
- 它不会把 oncewhere 硬塞进数学 agent 系统；它与主线的联系是主题性的，也是个人性的。

## 状态

这个地图是持续工作的文档。每张卡上的日期表示最近一次检查证据和措辞的时间。历史决策保存在 decisions/ 中，使路线可以改变，而不必抹掉它如何走到这里。

[English version](README.md)
