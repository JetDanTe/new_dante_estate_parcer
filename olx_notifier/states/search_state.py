from telebot import types
from olx_notifier.states.base import BaseState
from olx_notifier.tg_buttons import SearchButton


class SearchState(BaseState):
    text = "Вы выбрали: {user_filter[id]['city']}."

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(SearchButton.search)

    def process(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == f'nextstate:searchState':
                print("Start seacrhing!")
                return AdvViewer(self.chat_id, kv_filter)
        return self


