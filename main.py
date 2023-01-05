from gtts import gTTS

language = "en"
text = "Hello, world. I am a computer and I talk"

speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save("textToSpeech.mp3")
