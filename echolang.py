from transformers import pipeline
from gtts import gTTS
import os

# Supported languages
supported_langs = {
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}

print("Available Languages:")
for code, name in supported_langs.items():
    print(f"{code} → {name}")

# Select language
translation_lang_code = input("\nEnter target language code (hi/es/fr/de): ").strip().lower()

# Load model
model_name = f"Helsinki-NLP/opus-mt-en-{translation_lang_code}"
translator = pipeline(f"translation_en_to_{translation_lang_code}", model=model_name)

print(f"\nTranslator is ready (English to {supported_langs[translation_lang_code]})")

# Loop for translation
while True:
    text_en = input("\nEnter text in English (or type 'exit' to quit): ")
    if text_en.lower() == 'exit':
        break

    result = translator(text_en)
    translated_text = result[0]['translation_text']
    print(f"Translated: {translated_text}")

    tts = gTTS(text=translated_text, lang=translation_lang_code)
    tts.save("spoken.mp3")
    os.system("mpg123 spoken.mp3")  

