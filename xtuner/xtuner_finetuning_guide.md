# 使用 XTuner 微调模型：步骤指南


微调也经常被戏称为是炼丹，就是说你炼丹的时候你得思考好用什么样的材料、用多大的火候、烤多久的时间以及用什么丹炉去烧。这里的丹炉其实我们可以想象为
XTuner ，只要丹炉的质量过得去，炼丹的时候不会炸，一般都是没问题的。但是假如炼丹的材料（就是数据集）本来就是垃圾，那无论怎么炼（微调参数的调整），
炼多久（训练的轮数），炼出来的东西还只能且只会是垃圾。只有说用了比较好的材料，那么我们就可以考虑说要炼多久以及用什么办法去炼的问题。因此总的来说，
学会如何构建一份高质量的数据集是至关重要的。


本指南将详细介绍如何使用 XTuner 进行模型微调，重点解释相关命令及其使用方法。

## 步骤 1: 安装 XTuner

首先，确保您已经安装了 XTuner。可以使用以下命令安装：

```bash
pip install xtuner
```

## 步骤 2: 准备配置文件

XTuner 使用配置文件来定义微调过程。您可以使用预定义的配置文件或创建自定义配置。

### 列出预定义配置

使用以下命令查看所有预定义的配置文件：

```bash
xtuner list-cfg
```

### 复制预定义配置

如果想基于预定义配置进行修改，可以使用以下命令复制配置文件：

```bash
xtuner copy-cfg $CONFIG $SAVE_FILE
```

例如：
```bash
xtuner copy-cfg llama2_7b_chat_qlora path/to/your/custom_config.py
```

## 步骤 3: 自定义配置文件

编辑复制的配置文件，根据您的需求进行修改。主要关注以下几点：

1. 模型架构
2. 数据集设置
3. 训练参数（学习率、批次大小等）
4. 优化器设置
5. 学习率调度
6. 评估指标

## 步骤 4: 验证自定义数据集配置

如果您使用了自定义数据集，可以使用以下命令验证配置的正确性：

```bash
xtuner check-custom-dataset path/to/your/custom_config.py
```

## 步骤 5: 开始训练

### 单 GPU 训练

使用以下命令在单个 GPU 上进行训练：

```bash
xtuner train path/to/your/custom_config.py
```

您可以添加额外的参数来自定义训练过程：

```bash
xtuner train path/to/your/custom_config.py \
    --work-dir /path/to/save/outputs \
    --gpu-id 0 \
    --cfg-options model.pretrained=/path/to/pretrained/model \
                  optimizer.lr=1e-5 \
                  train_dataloader.batch_size=4
```

参数说明：
- `--work-dir`: 指定输出目录
- `--gpu-id`: 指定使用的 GPU ID
- `--cfg-options`: 用于覆盖配置文件中的设置

### 多 GPU 训练

对于多 GPU 训练，使用以下命令：

```bash
NPROC_PER_NODE=$NGPUS NNODES=$NNODES NODE_RANK=$NODE_RANK PORT=$PORT ADDR=$ADDR xtuner dist_train path/to/your/custom_config.py $GPUS
```

请根据您的环境设置相应的环境变量。

## 步骤 6: 监控训练过程

训练开始后，XTuner 会在指定的 `work-dir` 中生成日志文件。您可以通过查看这些日志来监控训练进度。

## 步骤 7: 评估模型

训练完成后，您可以使用以下命令评估模型：

```bash
xtuner test path/to/your/custom_config.py
```

## 步骤 8: 模型转换

### 将 PTH 模型转换为 HuggingFace 格式

```bash
xtuner convert pth_to_hf path/to/your/custom_config.py /path/to/pth/model /path/to/save/hf/model
```

### 合并 adapter 到预训练基础模型

```bash
xtuner convert merge $LLM $ADAPTER $SAVE_PATH
```

## 步骤 9: 与模型对话

使用以下命令与微调后的模型进行对话：

```bash
xtuner chat $LLM --adapter $ADAPTER --prompt-template $PROMPT_TEMPLATE
```

## 结语

以上就是使用 XTuner 进行模型微调的基本步骤。每个步骤都可以根据具体需求进行调整。如果遇到问题，可以查阅 XTuner 的官方文档或在 GitHub 上提出问题。

Remember: 微调是一个迭代的过程。您可能需要多次调整配置和参数以获得最佳结果。