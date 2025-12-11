"""
Translation helper. Uses googletrans if available (install: `pip install googletrans==4.0.0-rc1`).
If the library isn't installed, it simply returns the original text with a note.
"""
try:
from googletrans import Translator
_translator = Translator()
except Exception:
_translator = None




def translate_text(text: str, dest_lang: str = 'hindi') -> str:
"""Translate `text` into `dest_lang` (language name or ISO code).
If translator is not available, return an explanatory string.
"""
if not _translator:
return f"[translation unavailable] -> {text}"


# accept language names like 'hindi' and try to translate
try:
result = _translator.translate(text, dest=dest_lang)
return result.text
except Exception:
# fallback: try English
try:
result = _translator.translate(text, dest='en')
return result.text
except Exception:
return f"[translation failed] -> {text}"