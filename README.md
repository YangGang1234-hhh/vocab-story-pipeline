
# Vocab Story Pipeline (Local, Python)

多模型并发生成“爆笑故事记忆法” → 自动评分选优 → 生成图片提示词的内容流水线（本地方案）。

## 目录
- `data/words.csv`：词表（word, meaning, decompose）
- `src/`：源码（提示词模板、模型网关、评分与选优）
- `output/`：运行产物（候选故事、评分、最佳故事、图片提示词）

> 本仓库当前仅包含代码骨架。后续步骤：在本地克隆、安装依赖、配置 `.env`、运行。
