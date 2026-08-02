from src.speech_to_text import speech_to_text
from src.llm import generate_response
from src.text_to_speech import text_to_speech

audio_file = "audio/input.wav"

print("Converting speech to text...")
user_text = speech_to_text(audio_file)
print("User:", user_text)

print("Generating response...")
ai_response = generate_response(user_text)
print("AI:", ai_response)

print("Converting text to speech...")
text_to_speech(ai_response)

print("Done! Check audio/output.mp3")