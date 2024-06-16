# internlm2-math-7b 模型部署

OpenXLab 浦源平台以开源为核心，提供了一套完整的模型训练、部署、管理的解决方案。本文档介绍如何使用 OpenXLab 浦源平台部署
internlm2-math-7b 模型。

## 1. 模型准备

....

## 2. 上传模型

OpenXLab平台地址：https://openxlab.org.cn/home

### 2.2 上传模型

本小节为上传模型至 OpenXLab 模型中心的步骤如下

![upload_model](./image/upload_model.png)

#### 2.2.1 初始化 Git 配置

**Linux:**

安装 git 和 git lfs，命令如下

```shell
# install git
sudo apt-get update
sudo apt-get install git

# install git lfs
sudo apt-get update
sudo apt-get install git-lfs

# use git install lfs
git lfs install
```

&nbsp;
设置您的 Git 用户名，OpenXLab 使用你在平台的用户名作为 Git的用户名，具体获取路径，可登录 OpenXLab 后，点击个人头像下的
【账号信息】查看个人的用户名

![upload_model_step2](./image/upload_model_step2.png)

配置 Git Username，用于作为 Git 提交的身份标识。

```shell
git config --global user.name "Username"
```

需要将 Username 替换成你在 OpenXLab 平台上的用户名

配置 Git Email

```shell
git config --global user.email "email@email.com"
```

#### 2.2.2 拉取模型仓库

首先需要在 OpenXLab 先创建一个空模型仓库，填写模型仓库的基本信息，包括仓库名称、任务类型、访问权限等。

![upload_model_step3](./image/upload_model_step3.png)

创建完成空的模型仓库后，找到该仓库的 git 地址并拉取该空仓库至本地，空仓库的地址在模型文件的下载按钮下，如下所示

![upload_model_step4](./image/upload_model_step4.png)

#### 2.2.3 获取 Git Access Token

在 OpenXLab 的密钥管理添加 Git 令牌，步骤如下

![upload_model_step5](./image/upload_model_step5.png)

进入密钥管理页面，点击添加令牌，输入一个令牌名称和选择可写的权限，点击添加即可生成一个 Git 令牌. 添加完成后，复制生成的 Git
令牌，用于后续的模型上传。

#### 2.2.4 上传模型文件

将模型文件拷贝至本地的模型仓库目录下，然后执行以 git push 命令提交模型文件至 OpenXLab 平台. 在执行 git push
时会弹出身份验证的弹窗，填入 Username 和 Access Token 信息，如图所示

![img](./image/upload_model_step9.png)


### 2.3 编写代码

编写 chat 的 web-ui 代码， 主要包括项目结构初始化, 应用环境配置, 和 gradio 的部署代码。

![gradio_web_ui_step](./image/gradio_web_ui_step.png)

#### 2.3.1 初始化项目结构

创建一个新的 GitHub 仓库 https://github.com/1587causalai/PersonalizedLLM-gradio 来存放您的 gradio 应用代码。

```shell
├─GitHub_Repo_Name
│  ├─app.py                 # Gradio 应用默认启动文件为app.py，应用代码相关的文件包含模型推理，应用的前端配置代码
│  ├─requirements.txt       # 安装运行所需要的 Python 库依赖（pip 安装）
│  ├─packages.txt           # 安装运行所需要的 Debian 依赖项（ apt-get 安装）
|  ├─README.md              # 编写应用相关的介绍性的文档
│  └─... 
```

#### 2.3.2 配置应用环境

**依赖管理**：配置应用所需的运行环境,如有 Python 依赖项（ pip 安装）可写入 requirements.txt 中，Debian 依赖项（ apt-get 安装）可写入 packages.txt 中，并存放至代码仓库的根目录下。

requirement.txt 配置 python相关的依赖包，例如 gradio、torch、transformers 等

```text
gradio==4.10.0
transformers
sentencepiece
einops
accelerate
tiktoken
```

packages.txt 配置下载模型权重的工具包 git 和 git-lfs

```text
git
git-lfs
```

#### 2.3.3 部署 gradio

编写一个app.py文件，里面可以通过transformers框架进行模型实例化并通过gradio组件搭建chat聊天界面. 代码如下：

```python
import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

# clone the model from OpenXLab
base_path = './PersonalizedLLM'
os.system(f'git clone https://code.openxlab.org.cn/causalgpt/PersonalizedLLM.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')

tokenizer = AutoTokenizer.from_pretrained(base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path,trust_remote_code=True, torch_dtype=torch.float16).cuda()

def chat(message,history):
    for response,history in model.stream_chat(tokenizer,message,history,max_length=2048,top_p=0.7,temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="Personalized LLM Research Assistant",
                description="""
                 一个定制化的问答机器人,专注于为学者提供个性化大语言模型领域的专业知识和有价值的参考资料。
                 """,
                 ).queue(1).launch()

```
#### 2.3.4 推送代码至 GitHub

编写完应用代码，记得推动您的应用代码至 GitHub 仓库中

### 2.4 部署应用

本小节为在OpenXLab浦源平台中，部署写好的 chat web-ui 的应用，具体步骤如下。

![deploy-openxlab](./image/deploy-openxlab.png)

#### 2.4.1 创建入口

创建入口在导航栏的右侧 `+ 创建` ，如下如所示：

![create_step_1](./image/create_step_1.png)

选择Gradio组件，开始创建

![create_step_2](./image/create_step_2.png)


#### 2.4.2 应用配置

填写 Chat 应用的基础信息，包括应用的名称和应用对应的任务类型，并填入 GitHub 仓库的地址，选择硬件资源后，即可立即创建啦~

![create_step_3](./image/create_step_3.png)


**应用配置注意事项**

1. **GitHub 授权**：若未进行 GitHub 授权,请先前往授权
2. **自定义启动文件**：若您有需要自定义启动的文件,可以通过配置选择启动文件的路径
3. **资源申请**：若当前您的资源quota不能满足您的应用需求,也可以填写硬件资源申请表单进行 [申请获取](https://openxlab.org.cn/apps/apply-hardware)
 * 如需部署 InternLM2-7b 模型建议申请 8vCPU 32GB Nvidia A10 24GB 规格资源
 * 如需部署 InternLM2-20b 模型建议申请 12vCPU 48GB Nvidia A100 40GB 规格资源
4. **环境变量配置**：若您有不方便在代码中暴露的变量信息,可通过高级配置中的环境变量进行配置 

