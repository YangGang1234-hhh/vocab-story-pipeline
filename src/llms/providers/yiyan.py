
import httpx
from src.config import YIYAN_API_KEY, TIMEOUT_SECS

async def chat(prompt: str) -> str:
    if not YIYAN_API_KEY:
        return ""
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={YIYAN_API_KEY}"
    payload = {"messages":[{"role":"user","content":prompt}], "temperature":0.8}
    async with httpx.AsyncClient(timeout=TIMEOUT_SECS) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
        return data.get("result","")
