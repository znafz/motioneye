#controls the bot so that I don't have to rebuild every time to develop
import subprocess
import os
import signal
import time



if __name__ == "__main__":
    print("starting dev environment")
    cmd = ['python3', 'bot/bot.py']
    proc = subprocess.Popen(cmd)
    while(True):
        if (proc.poll() != None):
            print("restarting bot")
            proc = subprocess.Popen(cmd)
        if os.path.isfile("bot/kill"):
            proc.terminate()
            os.remove("kill")
        time.sleep(3)
