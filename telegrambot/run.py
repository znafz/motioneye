#controls the bot so that I don't have to rebuild every time to develop
import subprocess
import os
import signal

def check_pid(pid):        
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
pid = 0
while(True):
    if (not check_pid(pid)):
        cmd = ['python', 'bot/bot.py']
        pid = subprocess.Popen(cmd).pid
    if os.path.isfile("kill"):
        os.kill(pid, signal.SIGTERM)