---
id: contextswarm
title: "ContextSwarm"
theme: formal-proof-systems
status: collaborative-research
visibility: private
ownership: collaborative
repository: https://github.com/nustarai/ContextSwarm
last_reviewed: 2026-10-14
---

# ContextSwarm：FLT 证明进展分析与系统迭代

**团队项目中的个人贡献：** 证明进展分析、工具接口诊断、提示词迭代和实验问题修复。

## 团队产出与项目关系

ContextSwarm 围绕费马大定理（FLT）形式化重建开展长程多智能体研究。ProofState 维护目标、路线、依赖和验证状态；CPS 保存研究发现、失败经验与交接信息。团队形成协作系统、十项分层 Lean 重建任务组成的 FLTBench 和实验评估框架，产生 [ICLR 2027 阶段投稿](flt-iclr-stage-output.md)，后续形成 [AAMAS 2027 运行分析](flt-proof-weaving-aamas.md)。二者是同一项目的不同产出；整体 FLT 形式化目标尚未完成。

## 我的实际工作

我结合 FLT 证明结构、共享状态与运行记录，检查哪些局部结论已通过验证、哪些条件仍缺失，以及已有结果能否满足上层证明的需要。围绕这些问题，我整理《设想的长程证明推进方式》，参与提示词重构：从上层用途明确局部接口，让子问题随真实缺口展开，减少不必要的固定检查、强制拆分与注册要求，同时保留共享证明状态和可靠验证约束。

## 代表性诊断：对象存在，不等于工具能提供它的用途

一次运行中，Agent 无法获得当前子目标的上层用途，但事件记录表明它已被两条父路线使用。我沿证明关系检查接口，将问题定位为缺少从子目标反查父路线的查询能力，并提出、推动补齐这一接口。团队随后合并功能，专项验收观察到 Agent 能获得相关信息并继续工作。

这个案例支持的是一个具体信息缺口的诊断与修复，不是“该接口已在受控对照中提升整体 FLT 成功率”。我还处理了 FLTBench 预置证明资料的检索和分段读取问题，提出并探索 CPS 记录与多个数学节点双向关联的设计；后者不写成已经验证有效的完整系统。

## Evidence

已有[系统快照](https://github.com/nustarai/ContextSwarm/commit/1076e4e8a6d194870bbf0ce65303fbad8dd2a7e3)来自原项目索引。上面的具体诊断、合并和验收经过依据作者于 2026-10-14 提供的经历说明；**本卡尚未固定对应 PR 和验收日志，不把系统快照当作该案例的逐项证据。** 原始团队材料仍受访问限制。

## 贡献边界与下一问

完整系统、FLTBench 和投稿是团队成果，我不声称领导整个项目、独立实现全部组件或完成 ICLR 稿件写作。[ContextSwarmJudge](contextswarm-judge.md)只是关联验证组件，不是我的仓库贡献。

任务结构能提供组织依据，但未必给出最合适的协作方式。下一步是研究如何保留必要的验证约束，同时允许共享信息、工具接口和组织方式接受持续检验与修改。
