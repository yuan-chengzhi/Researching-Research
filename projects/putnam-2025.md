---
id: putnam-2025
title: "Putnam 2025: formal proof experiments"
theme: reliable-action-and-feedback
status: experimentally-observed
visibility: private
ownership: direct
repository: https://github.com/yuan-chengzhi/pi-math-first-proof-swarm
last_reviewed: 2026-10-14
---

# Putnam 2025：形式化证明闭环与 Lean 工具环境

**个人工作：** 实验平台、提示词、Lean 工具、运行排查与结果分析。实验使用 Putnam 2025 的题目；全题报告日期为 2026-06-22，不是参加官方竞赛的成绩。

## 问题与实际工作

当 Agent 能够反复尝试、检查、修正和从中断恢复时，形式化工具环境如何影响它的数学工作？我搭建并迭代 [Pi Math First Proof Swarm](pi-math-first-proof-swarm.md) 与 [pi-lean-tools](pi-lean-tools.md)，让声明和前提搜索、片段检查、局部证明尝试进入探索过程，而不只用于自然语言证明完成后的翻译。探索工具提供参考，最终是否通过由独立验证流程确定。

## 已有结果与口径

E13 全题报告记录：12 道题之间串行，每题八次并行尝试；任一尝试达到内部 `final_verified` 后结束该题其余尝试。12 题均达到这一内部标准。**约 5.5 小时是报告逐题运行用时的合计，不是包括所有失败运行、排查和修复的端到端耗时，也不是八条尝试的总 Agent-hours。**

报告还记录了 B3/B6 的验证器签名检查问题：零参数定理被错误地当作函数应用，导致候选反复被拒绝。实验使用隔离的修复版验证服务继续完成，没有据此声称修改了团队共享服务或向 `ContextSwarmJudge` 仓库贡献了代码。此处记录的是实验报告中的诊断；本仓库未重跑全部证明，也未收录当时的本地补丁。

## 一个改变设计判断的对照

在运行中断机制和 Lean 工具问题修复后，A5 的附加自然语言优先提示与不附加该提示两侧均完成证明；无附加提示的一侧也自行先推理、再生成 Lean 候选。这使我区分“提供必要的工作能力”和“规定工作顺序”。**单题、单次对照不足以证明某种流程普遍更优，也不能证明提示没有作用。**

## Evidence

| 材料 | 支持什么 | 不支持什么 |
| --- | --- | --- |
| [E13 全题报告（固定版本）](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/docs/thoughts/e13-putnam2025-full12-formal-sweep-zh.md) | 设置、逐题结果、运行口径和验证器排查记录 | 官方竞赛成绩、独立复现、一般数学研究能力 |
| [A5 两种提示设置分析（固定版本）](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/docs/thoughts/e12a-nlfirst-vs-formal-analysis-zh.md) | 两侧完成与实际工作顺序的记录 | 单次比较所不能支持的普遍优势或等价结论 |
| [全题编排脚本（固定版本）](https://github.com/yuan-chengzhi/pi-math-first-proof-swarm/blob/20c6e0342654265ad47f5c3c63fd9a013100232a/docs/experiments/e13/run_putnam12_formal.sh) | 题间串行和题内并行的执行设置 | 脚本本身不证明运行结果 |

原始来源为私有仓库；这里提供说明和定位，不暗示外部读者已经取得访问权限。

## 下一问

哪些工具和反馈确实改变了后续行动？随着任务变长、参与者增多，怎样保留可靠约束，同时让 Agent 自己选择有用的工作方式？
