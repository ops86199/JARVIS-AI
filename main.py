"""Entry point for the Jarvis assistant.
This wires together voice I/O, the brain (command handling), and the AI (Gemini).
Make sure your corrected jarvis.py is present and has a function `ask_gemini(prompt)`.
"""
import os
import jarvis
from voice import speak, listen
import brain




def main():
speak("Hello Omprakash, Jarvis is online. I am ready.")


while True:
command = listen()
if not command:
continue


# global exit keywords
if any(k in command for k in ("stop", "exit", "shutdown", "bye")):
speak("Okay, shutting down. Goodbye!")
break


# hand off to brain with the AI function
reply = brain.handle_command(command, ask_ai=jarvis.ask_gemini)


# brain can return a tuple (speak_text, continue_flag) or just a string
if isinstance(reply, tuple):
speak_text, cont = reply
speak(speak_text)
if cont is False:
break
else:
speak(reply)




if __name__ == "__main__":
main()
