
import httpx
from src.config import DEEPSEEK_API_KEY, TIMEOUT_SECS

MODEL = "deepseek-chat"

async def chat(prompt: str) -> str:
    if not DEEPSEEK_API_KEY:
        return ""
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    payload = {"model": MODEL, "messages":[{"role":"user","content":prompt}], "temperature":0.8}
    async with httpx.AsyncClient(timeout=TIMEOUT_SECS) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
