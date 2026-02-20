
IMAGE_PROMPT_TMPL = """
Create a bright, exaggerated, comedic cartoon illustration based on:
"{one_liner}"

Requirements:
- Show the English word "{word}" as comic-style glowing text (integrated in the scene).
- Show the Chinese meaning "{meaning}" inside a speech bubble or label.
- Exaggerated expressions, dynamic motion lines, strong focal point.
- Vibrant colors, thick outlines, non-horror, humorous.
- The scene must convey the meaning in 0.5 seconds.
""".strip()

def make_image_prompt(word: str, meaning: str, one_liner: str) -> str:
    return IMAGE_PROMPT_TMPL.format(word=word, meaning=meaning, one_liner=one_liner)
