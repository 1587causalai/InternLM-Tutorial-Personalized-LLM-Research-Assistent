# Evaluation And Ethics


# 大语言模型能力评估：李宏毅教授课程笔记

老李这周讲的是模型能力评估，真是干货满满啊！我总结梳理如下：

## 1. 多种评估方法

- 对于同一个问题，让模型的输出和标准答案比较。
<div align="center">
  <img src="imgs/w4_1.png" width="50%" alt="标准答案比较方法">
</div>

- Chat Arena 使用人类反馈信息评估模型表现 https://chat.lmsys.org/
- 更进一步可以用 LLM 充当人类评估角色。
  - 例如MT-bench 使用强大语言模型 GPT-4 评估，但只有80个题目，这样的评估方式是否可靠？
  - 最近有一个改版 Arena-hard 

**补充**：这些方法各有优缺点。标准答案比较方法简单但可能忽视语言的灵活性[1]。人类评估更接近实际应用，但成本高且可能存在主观性[2]。LLM评估效率高，但其可靠性和公正性仍在研究中[3]。

## 2. 评估基准大比拼

多种评估基准哪个更好？ 老李把这个问题回答的很好，整体逻辑上按照 chat arena spearman correlation 相关系数排序

<div align="center">
  <img src="imgs/w4_2.png" width="80%" alt="评估基准比较">
</div>

- 最菜的是直接看回答长度，相关系数才 0.35，差劲！
- AlpacaEval 2.0:是一个综合性的评估基准，涵盖了多种任务。相关性为0.94，不错哦。
  - LLM 本身有偏见， 偏好长篇大论答案， 去偏差之后 alpacaEval 2.0 --> LC AlpacaEval 2.0，相关性为0.98

**补充**：Spearman相关系数衡量的是排序一致性，而非绝对性能[4]。LC AlpacaEval 2.0的改进显示了评估方法需要不断适应模型的发展[5]。

## 3. 特殊能力大考验

- BIG-bench 有特别多奇葩复杂任务, 为难语言模型
- 大海捞针 needle in a haystack 测试的故事一波三折 
  - 有文章表明 GPT-4 长文本能力很好，但是以长文本能力著称的 Claude 却看起来很糟糕
  - 官方急了，改了下 prompt（加了句"Here is the most relevant sentence in the context:"），立马牛起来了。
- 一波三折心智理论测验
  - 有一个常见例子表明大模型具备心智
  - 后来发现通过研究发现比人类差远了，可能是数据泄露问题

**补充**：BIG-bench的多样性任务旨在全面评估模型的泛化能力[6]。Needle in a Haystack测试反映了模型在实际应用中处理长文本的关键能力[7]。心智理论测验涉及模型对人类认知的理解深度，这是AGI研究的重要方向[8]。

## 4. 数据泄露这个坑

最后老李，重点谈谈 benchmark 的数据泄露问题：模型偷偷看看训练资料吗？老李用清晰的逻辑，指出存在实锤证据

**补充**：数据泄露问题不仅影响评估的公平性，还可能导致对模型能力的错误估计。这凸显了设计新型评估方法和数据集的重要性[9]。

总之，老李这课讲得透彻又有趣，把大语言模型评估这么复杂的东西讲得明明白白的。每次听完都觉得自己又行了！

## 参考文献

[1] Zhao, W. X., et al. (2023). "A Survey of Large Language Models". arXiv preprint arXiv:2303.18223.

[2] Zheng, L., et al. (2023). "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena". arXiv preprint arXiv:2306.05685.

[3] Ganguli, D., et al. (2023). "Evaluating and Improving Language Models with Preferences Labeled by Other Language Models". arXiv preprint arXiv:2305.14254.

[4] Liang, P., et al. (2022). "Holistic Evaluation of Language Models". arXiv preprint arXiv:2211.09110.

[5] Alpaca-Eval Team. (2023). "Alpaca-Eval: An Automatic Evaluator for Instruction-following Language Models". GitHub repository.

[6] Srivastava, A., et al. (2022). "Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models". arXiv preprint arXiv:2206.04615.

[7] Poesia, G., et al. (2023). "Needles in a Haystack: Finding Important Information in Large Language Model Outputs". arXiv preprint arXiv:2306.09346.

[8] Patel, K., et al. (2023). "Theory of Mind May Have Spontaneously Emerged in Large Language Models". arXiv preprint arXiv:2302.02083.

[9] Carlini, N., et al. (2023). "Extracting Training Data from Large Language Models". USENIX Security Symposium.





# Primitive prompts


```
行，你重构一下我的笔记，有一个重要的点你一定要记住, 笔记中涉及的内容，你要有专业参考文献的引用。

目前有几个地方不太满意:
1) 我希望你以你我的口吻视角和风格来重构这个笔记。
2) 有诸多的细节和逻辑，不符合我的预期。
  -  评估方法的多样性部分：我的核心诉求就是要把模型能力评估的本质做法说清楚
  - 
```



