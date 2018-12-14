import time
import sys
import telepot
import os
import fnmatch
from pprint import pprint

if __name__ == "__main__":
    with open('bot/apiKey', 'r') as keyfile:
        with open('bot/userid', 'r') as useridfile:
            token = keyfile.readline()
            user = useridfile.readline()
            bot = telepot.Bot(token)
            print(bot.getUpdates())
            latest = ""
            while(True):
                files = []
                for root, dirnames, filenames in os.walk('/var/lib/motioneye/'):
                    for filename in fnmatch.filter(filenames, '*.mp4'):
                        files.append(os.path.join(root, filename))
                temp = max(files, key=os.path.getctime)
                if(temp != latest):
                    print(temp)
                    latest = temp
                time.sleep(5)