from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
result = translator("I am a student.", max_length=40)
print(result[0]['translation_text'])

