
SCORE_PROMPT = """
你是“单词记忆工程”专家，请为下面候选故事打分并输出 JSON。

目标单词：{word}
中文含义：{meaning}

评分维度（0–10）：
- humor       搞笑程度
- meaning     词义贴合度
- spelling    拼写/读音拆分自然度
- image       可图像化程度
- memory      记忆强度

请对每个候选故事给出五个分数与一句理由，并计算 avg 平均分。
最后挑选得分最高的前 2 个，给出它们的索引列表 best_indices。

输出**严格**为 JSON，不要任何额外说明：
{
  "items": [
     {"index": 0, "scores": {"humor": 9, "meaning": 10, "spelling": 10, "image": 9, "memory": 10}, "avg": 9.6, "reason": "..."},
     ...
  ],
  "best_indices": [3, 1]
}

候选（索引 0..N）：
{stories}
""".strip()
