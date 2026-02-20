
import orjson
from pathlib import Path
from src.utils.json_io import dump_json
from src.pipeline.score_prompt import SCORE_PROMPT
from src.pipeline.image_prompt import make_image_prompt
from src.pipeline.select import to_one_liner
from src.config import JUDGE_PROVIDER
from src.llms.providers import gpt, deepseek

async def _judge(provider: str, prompt: str) -> str:
    if provider == "deepseek":
        return await deepseek.chat(prompt)
    return await gpt.chat(prompt)

def score_and_select(word: str, meaning: str, stories: list, out_dir: Path):
    cands = [s["story"] for s in stories]
    payload = "\n\n".join([f"#{i}: {s}" for i, s in enumerate(cands)])
    prompt = SCORE_PROMPT.format(word=word, meaning=meaning, stories=payload)

    import asyncio
    judge_text = asyncio.run(_judge(JUDGE_PROVIDER, prompt))

    try:
        data = orjson.loads(judge_text)
    except Exception:
        data = {"items": [], "best_indices": [0]}

    dump_json(data, out_dir / "scored" / f"{word}.json")

    best_ids = data.get("best_indices", [0])[:2] or [0]
    best = [{"index": i, "story": cands[i]} for i in best_ids]

    primary = best[0]["story"]
    one_liner = to_one_liner(primary)
    img_prompt = make_image_prompt(word, meaning, one_liner)

    dump_json({"word": word, "best": best, "one_liner": one_liner, "image_prompt": img_prompt},
              out_dir / "best" / f"{word}.json")
    (out_dir / "image_prompts").mkdir(parents=True, exist_ok=True)
    (out_dir / "image_prompts" / f"{word}.txt").write_text(img_prompt, encoding="utf8")

    return best, img_prompt
