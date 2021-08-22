from telebot import types
from olx_notifier.config import price_chooser

from olx_notifier.states.base import BaseState
from olx_notifier.states.search_state import SearchState
from olx_notifier.tg_buttons import PriceStateButtons
from pprint import pprint


class CityState(BaseState):
    text = "Поиск по {тут должна быть переменная которая будет меняться в зависимости от кнопки}, выбери цену:"

    def __init__(self, user_filter,  chat_id=None):
        super().__init__(chat_id)
        print('Мы вошли в конструктор!')
        self.user_filter = user_filter
        self.keyboard.add(PriceStateButtons.f2t5State)
        self.keyboard.add(PriceStateButtons.f5t7State)
        self.keyboard.add(PriceStateButtons.f7t10State)
        self.list_of_prices = ['f2t5State', 'f5t7State', 'f7t10State']

    def process(self, message: types.Message):
        print(message)
        pprint(message)
        if hasattr(message, 'data'):
            for price in self.list_of_prices:
                print(price)
                if message.data == f'nextstate:{price}State':
                    a, b = price_chooser(price)
                    self.user_filter[self.chat_id]['min_pr'] = a
                    self.user_filter[self.chat_id]['max_pr'] = b
                    print(f"Min price:{self.user_filter[self.chat_id]['min_pr']}"
                          f"\nMax price:{self.user_filter[self.chat_id]['max_pr']}")
                    return SearchState(self.chat_id)
        return self
