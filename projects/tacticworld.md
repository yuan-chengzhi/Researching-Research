---
id: tacticworld
title: "TacticWorld"
theme: reliable-action-and-feedback
status: design
visibility: private
ownership: direct
repository: https://github.com/yuan-chengzhi/TacticWorld
last_reviewed: 2026-10-14
---

# TacticWorld：学习证明动作的后果

**个人探索；研究设计与初步工具链工作。完整训练和比较评估尚未完成。**

## 问题与方案

2026 年 7 月参加强化学习暑期学校期间，我探索：模型能否从同一个 Lean 证明状态下不同 tactic 的真实执行后果中，学习失败类型、状态变化和后续行动选择，而不只学习成功证明轨迹？

方案从同一状态执行多个候选动作，保留成功、失败及结构化状态变化；在可比的模型、训练 token、优化步数与后续证明监督下，比较“只学习成功转移”与“学习多种动作后果”。这是待检验的比较，不是已得到的泛化或样本效率提升。

## 我的工作与当前状态

我设计了数据构造与比较方案，并开展工具链搭建和初步流程探索。可核对的仓库 README 记录了 2026-07-12 的计划和 2026-07-17 的初始化；工具链探索进展来自作者的补充说明，不由这份早期 README 单独证明。

## Evidence

[研究设计与状态说明（固定版本）](https://github.com/yuan-chengzhi/TacticWorld/blob/766780c1a780a633954341d921422ae0d3562df5/README.md)。来源仓库为私有。固定版本支持研究问题和对照设计的存在，不支持训练已经完成。

## 与研究主线的关系

这是一条关于局部行动与反馈学习的并行探索，不是已经实现的群体自主演化机制，也不应为了制造一条整齐时间线而被写成所有后续项目的前置阶段。
