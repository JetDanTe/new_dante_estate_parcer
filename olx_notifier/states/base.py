from telebot import types

from olx_notifier.config import bot
from olx_notifier.models import Client


class BaseState:
    text: str = ""
    keyboard = None

    def __init__(self, chat_id):
        # self.text = text
        self.chat_id = chat_id
        keyboard = types.InlineKeyboardMarkup()
        self.keyboard = keyboard
        self.user = self.get_user()


    def display(self):
        if not self.text == '':
            bot.send_message(self.chat_id, self.text, reply_markup=self.keyboard)

    def proccess(self, message: types.Message):
        return self

    def get_user(self) -> Client:
        if not Client.objects.filter(chat_id=self.chat_id).exists():
            return Client.objects.create(chat_id=self.chat_id, settings={}, user_name='', last_viewed='')
        return Client.objects.filter(chat_id=self.chat_id).first()



