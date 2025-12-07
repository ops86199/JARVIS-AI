import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# ---------------------------
# 1. Configure Gemini API
# ---------------------------
genai.configure(api_key="YOUR_API_KEY_HERE")

# Gemini model
model = genai.GenerativeModel("gemini-pro")

# ---------------------------
# 2. Text-to-Speech (Voice Output)
# ---------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)   # speaking speed
engine.setProperty("volume", 1.0) # max volume

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------------------
# 3. Speech-to-Text (Voice Input)
# ---------------------------
listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            text = listener.recognize_google(audio)
            print("You:", text)
            return text
    except:
        return ""

# ---------------------------
# 4. JARVIS Brain (Gemini Response)
# ---------------------------
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# ---------------------------
# 5. Conversation Loop
# ---------------------------
def start_jarvis():
    speak("Hello Omprakash, I am online. You can talk to me now.")

    while True:
        command = listen()

        if command == "":
            continue

        if "stop" in command.lower() or "exit" in command.lower():
            speak("Okay, shutting down. Goodbye!")
            break

        reply = ask_gemini(command)
        speak(reply)


# ---------------------------
# Start JARVIS
# ---------------------------
start_jarvis()
