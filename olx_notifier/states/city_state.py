from telebot import types
from olx_notifier.config import price_chooser

from olx_notifier.states.base import BaseState
from olx_notifier.states.search_state import SearchState
from olx_notifier.tg_buttons import PriceStateButtons
from pprint import pprint


class CityState(BaseState):
    text = "Выбери бюджет, пожалуйста."

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(PriceStateButtons.f2t5State)
        self.keyboard.add(PriceStateButtons.f5t7State)
        self.keyboard.add(PriceStateButtons.f7t10State)
        self.list_of_prices = ['f2t5', 'f5t7', 'f7t10']

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            for price in self.list_of_prices:
                if message.data == f'nextstate:{price}State':
                    a, b = price_chooser(price)
                    user = self.get_user()
                    user.settings['min_pr'] = a
                    user.settings['max_pr'] = b
                    user.save()
                    return SearchState(self.chat_id)
        return self
