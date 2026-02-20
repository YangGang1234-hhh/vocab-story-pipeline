
import httpx
from src.config import QWEN_API_KEY, TIMEOUT_SECS

MODEL = "qwen-plus"

async def chat(prompt: str) -> str:
    if not QWEN_API_KEY:
        return ""
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {"Authorization": f"Bearer {QWEN_API_KEY}"}
    payload = {"model": MODEL, "messages":[{"role":"user","content":prompt}], "temperature":0.8}
    async with httpx.AsyncClient(timeout=TIMEOUT_SECS) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
