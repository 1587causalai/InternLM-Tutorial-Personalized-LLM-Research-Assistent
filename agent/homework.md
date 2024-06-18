# 作业

> [!TIP]
> 结营必做基础作业；优秀学员或进入对应 SIG 需完成进阶作业。

## 基础作业（结营必做）

1. 完成 Lagent Web Demo 使用，并在作业中上传截图。文档可见 [Lagent Web Demo](lagent.md#1-lagent-web-demo)
2. 完成 AgentLego 直接使用部分，并在作业中上传截图。文档可见 [直接使用 AgentLego](agentlego.md#1-直接使用-agentlego)。

## 进阶作业（优秀必做）

1. 完成 AgentLego WebUI 使用，并在作业中上传截图。文档可见 [AgentLego WebUI](agentlego.md#2-作为智能体工具使用)。
2. 使用 Lagent 或 AgentLego 实现自定义工具并完成调用，并在作业中上传截图。文档可见：
    - [用 Lagent 自定义工具](lagent.md#2-用-lagent-自定义工具)
    - [用 AgentLego 自定义工具](agentlego.md#3-用-agentlego-自定义工具)

## 大作业选题

### 算法方向

1. 在 Lagent 或 AgentLego 中实现 RAG 工具，实现智能体与知识库的交互。
2. 基于 Lagent 或 AgentLego 实现工具的多轮调用，完成复杂任务。如：智能体调用翻译工具，再调用搜索工具，最后调用生成工具，完成一个完整的任务。
3. ...

### 应用方向

1. 基于 Lagent 或 AgentLego 实现一个客服智能体，帮助用户解决问题。
2. 基于 Lagent 或 AgentLego 实现一个智能体，实现艺术创作，如生成图片、视频、音乐等。
3. ...

---

## Lagent 构建智能体

Lagent 是一个轻量级开源智能体框架，旨在让用户可以高效地构建基于大语言模型的智能体。同时它也提供了一些典型工具以增强大语言模型的能力。

Lagent 的 Web Demo 需要用到 LMDeploy 所启动的 api_serve:

```bash
conda activate agent
lmdeploy serve api_server /root/share/new_models/Shanghai_AI_Laboratory/internlm2-chat-7b \
                            --server-name 127.0.0.1 \
                            --model-name internlm2-chat-7b \
                            --cache-max-entry-count 0.1
```

Lagent 是一个轻量级开源智能体框架，旨在让用户可以高效地构建基于大语言模型的智能体。同时它也提供了一些典型工具以增强大语言模型的能力。

Lagent 的 Web Demo 需要用到 LMDeploy 所启动的 api_serve:

```bash
conda activate agent
lmdeploy serve api_server /root/share/new_models/Shanghai_AI_Laboratory/internlm2-chat-7b \
                            --server-name 127.0.0.1 \
                            --model-name internlm2-chat-7b \
                            --cache-max-entry-count 0.1
```

23333端口是由 LMDeploy 的 api_server 服务使用的。在启动 LMDeploy api_server 时，可以通过 --port
参数指定服务监听的端口。如果没有显式指定端口，LMDeploy 会默认使用23333端口。
新建一个 terminal 以启动 Lagent Web Demo。在新建的 terminal 中执行如下指令：

```bash
conda activate agent
cd /root/agent/lagent/examples
streamlit run internlm2_agent_web_demo.py --server.address 127.0.0.1 --server.port 7860
```

在等待 LMDeploy 的 api_server 与 Lagent Web Demo 完全启动后，在**本地**进行端口映射，将 LMDeploy api_server 的23333端口以及
Lagent Web Demo 的7860端口映射到本地。可以执行：

```bash
ssh -CNg -L 7860:127.0.0.1:7860 -L 23333:127.0.0.1:23333 root@ssh.intern-ai.org.cn -p 36047
```

接下来在本地的浏览器页面中打开 http://localhost:7860 以使用 Lagent Web Demo。
首先输入模型 IP 为 127.0.0.1:23333，**在输入完成后按下回车键以确认**。并选择插件为 ArxivSearch，以让模型获得在 arxiv
上搜索论文的能力。

我们输入“请帮我搜索 InternLM2 Technical Report” 以让模型搜索书生·浦语2的技术报告。效果如下图所示，可以看到模型正确输出了
InternLM2 技术报告的相关信息。尽管还输出了其他论文，但这是由 arxiv 搜索 API 的相关行为导致的。

新建一个 terminal 以启动 Lagent Web Demo。在新建的 terminal 中执行如下指令：

```bash
conda activate agent
cd /root/agent/lagent/examples
streamlit run internlm2_agent_web_demo.py --server.address 127.0.0.1 --server.port 7860
```

在等待 LMDeploy 的 api_server 与 Lagent Web Demo 完全启动后，在**本地**进行端口映射，将 LMDeploy api_server 的23333端口以及
Lagent Web Demo 的7860端口映射到本地。可以执行：

```bash
ssh -CNg -L 7860:127.0.0.1:7860 -L 23333:127.0.0.1:23333 root@ssh.intern-ai.org.cn -p 36047
```

接下来在本地的浏览器页面中打开 http://localhost:7860 以使用 Lagent Web Demo。
首先输入模型 IP 为 127.0.0.1:23333，**在输入完成后按下回车键以确认**。并选择插件为 ArxivSearch，以让模型获得在 arxiv
上搜索论文的能力。

我们输入“请帮我搜索 InternLM2 Technical Report” 以让模型搜索书生·浦语2的技术报告。效果如下图所示，可以看到模型正确输出了
InternLM2 技术报告的相关信息。尽管还输出了其他论文，但这是由 arxiv 搜索 API 的相关行为导致的。

![搜索 InternLM2 技术报告](./assets/lagent/tech_output.png)