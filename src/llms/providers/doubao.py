
import httpx
from src.config import DOUBAO_API_KEY, TIMEOUT_SECS

MODEL = "ep-your-model"  # 替换为你的实际 Endpoint/模型名

async def chat(prompt: str) -> str:
    if not DOUBAO_API_KEY:
        return ""
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    headers = {"Authorization": f"Bearer {DOUBAO_API_KEY}"}
    payload = {"model": MODEL, "messages":[{"role":"user","content":prompt}], "temperature":0.8}
    async with httpx.AsyncClient(timeout=TIMEOUT_SECS) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
