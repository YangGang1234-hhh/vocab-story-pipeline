
import asyncio
from typing import List, Dict
from tenacity import retry, wait_exponential_jitter, stop_after_attempt
from .providers import gpt, deepseek, dobao, qwen, yiyan, kimi

PROVIDERS = [
    ("gpt", gpt.chat),
    ("deepseek", deepseek.chat),
    ("dobao", dobao.chat),
    ("qwen", qwen.chat),
    ("yiyan", yiyan.chat),
    ("kimi", kimi.chat),
]

@retry(wait=wait_exponential_jitter(0.5, 2), stop=stop_after_attempt(3))
async def _safe_call(name, fn, prompt):
    text = await fn(prompt)
    return {"model": name, "text": text or ""}

async def call_all_models_async(prompt: str) -> List[Dict]:
    tasks = [_safe_call(n, f, prompt) for n, f in PROVIDERS]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    ok = []
    for r in results:
        if isinstance(r, Exception):
            continue
        if r["text"]:
            ok.append(r)
    return ok

def call_all_models(prompt: str) -> List[Dict]:
    return asyncio.run(call_all_models_async(prompt))
