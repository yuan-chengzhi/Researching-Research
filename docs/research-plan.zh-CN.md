# 未来研究方向

> 状态：计划中的研究方向。当前地图中的任何 repo 都没有实现这个系统。

这个问题从现有项目自然长出来：当形式化数学工作变得更长、更协作化，并且需要在 agent 之间反复 handoff 时，怎样让它仍然有用？

未来系统会研究 proof work 周围的 research substrate：

- 保存哪些对象，包括 goal、candidate lemma、certificate、未解决义务、脚本、trace 和 provenance；
- 对象之间如何连接，同时把数学证据与 retrieval、通信分开；
- 临时对象在什么条件下可以安全继承；
- 观察一次运行之后，如何选择更好的挑战或 handoff。

第一轮实验应该固定模型、Lean toolchain、verifier、预算和评估边界，一次只改变一个 substrate 选择。目标是检验结构化状态是否改善 continuation 和 reuse，而不是预设更复杂的组织一定更好。

这会作为独立的研究计划展开。当前地图只记录问题为何出现，并为下一个 repo、artifact 或负结果保留位置，让研究可以继续改变它。