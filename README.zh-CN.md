# Researching Research

## 自主数学工作的条件

这是一个关于“数学工作如何在上下文窗口、会话或单个 agent 结束之后仍然有用”的活研究地图。

核心问题是：

> 一个 agent 周围需要有什么，长时间的数学工作才会变得可以积累、检查和替换？

这里收集的项目都围绕这个问题展开。有些项目构建形式化工具，有些表示未完成的工作，有些尝试建立持久研究世界或协调基础设施。与此同时，oncewhere 是一件相邻的创作：它提出了一个具有个人意味的问题——一段共同经历结束之后，什么应该仍然可以被保存、返回和理解？

这个仓库是研究路线的地图，不是 monorepo，也不是完成品清单。每个项目保留自己的身份和证据；随着证据变化，地图本身也可以变化。

## 如何阅读

1. 先看[研究路线](research-arc.md)，理解问题如何连接。
2. 再看[当前问题](current-questions.md)，了解真正还没有解决的部分。
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
