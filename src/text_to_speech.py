from gtts import gTTS

def text_to_speech(text, output_file="audio/output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)