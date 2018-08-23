import time
import sys
import telepot
from pprint import pprint

if __name__ == "__main__":
    with open('bot/apiKey', 'r') as keyfile:
        token = keyfile.readline()
        bot = telepot.Bot(token)
        pprint(bot.getUpdates())