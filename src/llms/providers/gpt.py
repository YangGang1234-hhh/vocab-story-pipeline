
import httpx
from src.config import OPENAI_API_KEY, TIMEOUT_SECS

MODEL = "gpt-4.1-mini"

async def chat(prompt: str) -> str:
    if not OPENAI_API_KEY:
        return ""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {"model": MODEL, "messages":[{"role":"user","content":prompt}], "temperature":0.8}
    async with httpx.AsyncClient(timeout=TIMEOUT_SECS) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
