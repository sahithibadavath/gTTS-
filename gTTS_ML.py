from gtts import gTTS
import os

from gtts.lang import tts_langs
print(tts_langs())

text = "HELL0, MY SELF blessy iam getting headche." 
language = 'en'
gTTS(text=text, lang='en').save("spoken.mp3")
os.system("start spoken.mp3")  # Use "afplay" on macOS or "xdg-open" on Linux
