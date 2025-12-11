"""
return True


if 'notepad' in name or 'editor' in name:
if os_name == 'windows':
subprocess.Popen(['notepad.exe'])
elif os_name == 'darwin':
subprocess.Popen(['open', '-a', 'TextEdit'])
else:
# try gedit, then xdg-open as fallback
try:
subprocess.Popen(['gedit'])
except Exception:
subprocess.Popen(['xdg-open', os.path.expanduser('~')])
return True


return False




def set_volume(percent: int):
"""Set system volume where supported. percent: 0-100"""
os_name = platform.system().lower()
percent = max(0, min(100, int(percent)))


try:
if os_name == 'linux':
# requires amixer
subprocess.call(['amixer', 'sset', 'Master', f'{percent}%'])
return True
elif os_name == 'darwin':
# macOS: use AppleScript
subprocess.call(['osascript', '-e', f'set volume output volume {percent}'])
return True
elif os_name == 'windows':
# Windows: no simple builtin command; leave as a no-op and inform user
print('Volume control on Windows requires extra package (not implemented).')
return False
except Exception as e:
print('Failed to set volume:', e)
return False




def shutdown():
os_name = platform.system().lower()
if os_name == 'windows':
os.system('shutdown /s /t 5')
elif os_name == 'darwin' or os_name == 'linux':
os.system('shutdown -h +0')
