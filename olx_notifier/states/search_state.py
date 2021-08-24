from telebot import types

from olx_notifier.config import bot
from olx_notifier.states.base import BaseState
from olx_notifier.tg_buttons import SearchButton
from olx_notifier.states.advviewer_state import AdvViewer
from olx_notifier import olx


class SearchState(BaseState):
    text = ""

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()
        bot.send_message(self.chat_id, f"Вы выбрали: {self.user.settings['city']}\nДиапазон цен: "
                                       f"от {self.user.settings['min_pr']} "
                                       f"до {self.user.settings['max_pr']}.",
                         reply_markup=self.keyboard.add(SearchButton.search))

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:searchState':
                return AdvViewer(self.chat_id)
        return self
