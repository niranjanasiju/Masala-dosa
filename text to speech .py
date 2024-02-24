from gtts import gTTS
import os

# Text you want to convert to speech
text = "Hello, how are you today?"

# Language in which you want to convert
language = "en"  # English

# Pass text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted audio
os.system("open output.mp3")
