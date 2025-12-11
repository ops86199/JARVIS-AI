"""
Text-to-speech and speech-to-text helpers using pyttsx3 and SpeechRecognition.
These are kept intentionally simple.
"""
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


recognizer = sr.Recognizer()




def speak(text: str):
"""Speak the provided text and also print to console."""
print("JARVIS:", text)
try:
engine.say(text)
engine.runAndWait()
except Exception as e:
print("TTS error:", e)




def listen(timeout: int = 5, phrase_time_limit: int = 8) -> str:
"""Listen from microphone and return recognized text (lowercase).
Returns empty string if nothing recognized.
"""
try:
with sr.Microphone() as source:
recognizer.adjust_for_ambient_noise(source, duration=0.3)
print("Listening...")
audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
text = recognizer.recognize_google(audio)
print("You:", text)
return text.lower()
except sr.WaitTimeoutError:
print("Listening timed out")
return ""
except sr.UnknownValueError:
print("Could not understand audio")
return ""
except Exception as e:
print("Microphone error:", e)
return ""
