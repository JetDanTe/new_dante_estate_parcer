import os

import telebot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAM')

bot = telebot.TeleBot(token)


def price_chooser(state):
    if state == 'f2t5State':
        min_pr = 2000
        max_pr = 5000
        return min_pr, max_pr
    if state == 'f5t7State':
        min_pr = 5000
        max_pr = 7000
        return min_pr, max_pr
    if state == 'f7t10State':
        min_pr = 7000
        max_pr = 10000
        return min_pr, max_pr
