
import re

def parse_stories(text: str):
    m = re.split(r"(?i)Story\s*1\s*:\s*", text, maxsplit=1)
    if len(m) < 2:
        return []
    s12 = re.split(r"(?i)Story\s*2\s*:\s*", m[1], maxsplit=1)
    s1 = s12[0].strip()
    s2 = s12[1].strip() if len(s12) > 1 else ""
    return [s for s in (s1, s2) if s]

def to_one_liner(story: str) -> str:
    s = re.split(r"[。.!?]\s*", story.strip())[0]
    return (s[:120] + "…") if len(s) > 120 else s
