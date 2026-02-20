
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DOUBAO_API_KEY = os.getenv("DOUBAO_API_KEY", "")
QWEN_API_KEY = os.getenv("QWEN_API_KEY", "")
YIYAN_API_KEY = os.getenv("YIYAN_API_KEY", "")
KIMI_API_KEY = os.getenv("KIMI_API_KEY", "")

JUDGE_PROVIDER = os.getenv("JUDGE_PROVIDER", "gpt")
IMAGE_PROVIDER = os.getenv("IMAGE_PROVIDER", "none")

TIMEOUT_SECS = 60
