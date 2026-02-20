
from pathlib import Path
import orjson

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def dump_json(obj, path: Path):
    ensure_dir(path.parent)
    path.write_bytes(orjson.dumps(obj, option=orjson.OPT_INDENT_2 | orjson.OPT_NAIVE_UTC))

def load_json(path: Path, default=None):
    if not path.exists():
        return default
    return orjson.loads(path.read_bytes())
