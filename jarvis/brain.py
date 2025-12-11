"""


def handle_command(command: str, ask_ai):
"""Process a user command and return a reply.
- `ask_ai` should be a function that accepts a prompt and returns text.
Returns either a string (reply text) or (reply_text, continue_flag).
"""
cmd = command.lower()


# time / date
if "time" in cmd:
now = datetime.datetime.now()
return f"Current time is {now.strftime('%I:%M %p')}"


if "date" in cmd:
now = datetime.datetime.now()
return f"Today's date is {now.strftime('%B %d, %Y')}"


# open website
if cmd.startswith("open "):
# example: "open youtube" or "open google.com"
target = command[5:].strip()
# try to form a url
if '.' in target:
url = target if target.startswith('http') else f'https://{target}'
else:
url = f'https://{target}.com'
webbrowser.open(url)
return f"Opening {target}"


# translate command: "translate hello to hindi"
if cmd.startswith("translate "):
# naive parsing: translate <text> to <lang>
try:
parts = command.split(" to ")
text_part = parts[0].replace("translate ", "", 1).strip()
lang = parts[1].strip()
translated = translate_text(text_part, dest_lang=lang)
return translated
except Exception:
return "Please say: translate <text> to <language>"


# if none of above, forward to AI
try:
ai_reply = ask_ai(command)
return ai_reply
except Exception:
return "Sorry, I couldn't get an answer from the AI."
