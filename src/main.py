
import argparse
from pathlib import Path
from rich import print
from tqdm import tqdm
from src.utils.json_io import dump_json
from src.pipeline.story_prompt import STORY_PROMPT
from src.llms.llm_gateway import call_all_models
from src.pipeline.select import parse_stories
from src.orchestrator import score_and_select

OUT = Path("output")

def run_one(word: str, meaning: str, decompose: str):
    prompt = STORY_PROMPT.format(word=word, meaning=meaning, decompose=decompose or "若不自然可略过")
    results = call_all_models(prompt)

    all_stories = []
    for r in results:
        s12 = parse_stories(r["text"])
        for s in s12:
            all_stories.append({"model": r["model"], "story": s})

    dump_json(all_stories, OUT / "raw_stories" / f"{word}.json")
    best, img_prompt = score_and_select(word, meaning, all_stories, OUT)

    print(f"[green]完成：{word}[/green]")
    print(f"最佳故事与图片提示词已写入 output/best/ 与 output/image_prompts/")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--word", type=str)
    ap.add_argument("--meaning", type=str)
    ap.add_argument("--decompose", type=str, default="")
    ap.add_argument("--csv", type=str, help="路径：data/words.csv；列：word,meaning,decompose")
    args = ap.parse_args()

    if args.csv:
        import csv
        with open(args.csv, encoding="utf8") as f:
            rows = list(csv.DictReader(f))
        for row in tqdm(rows, desc="批量生成"):
            run_one(row["word"], row["meaning"], row.get("decompose",""))
    else:
        assert args.word and args.meaning
        run_one(args.word, args.meaning, args.decompose)

if __name__ == "__main__":
    main()
