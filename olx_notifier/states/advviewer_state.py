from telebot import types

from olx_notifier import olx
from olx_notifier.states.base import BaseState
from olx_notifier.config import bot
from olx_notifier.tg_buttons import SearchButton, ChangeFilterButton


class AdvViewer(BaseState):
    text = ""

    def __init__(self, list_of_advs:list, chat_id, user_filter):
        super().__init__(chat_id)
        self.user_filter = user_filter
        self.chat_id = chat_id
        last_adv = list_of_advs[6]['id']
        for adv in list_of_advs[6:]:
            adv_formatted = f"{adv['title']}\n{adv['price']}\n{adv['description']}\n{adv['link']}"
            bot.send_message(self.chat_id, adv_formatted, reply_markup=self.keyboard)
        bot.send_message(self.chat_id, "Искать снова?", reply_markup=self.keyboard)
        self.keyboard.add(SearchButton.search)
        self.keyboard.add(ChangeFilterButton.change_filter)

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:searchState':
                parcer = olx.OlxApi(self.user_filter[self.chat_id], 232145135)
                return AdvViewer(parcer.get_adv(), self.chat_id, self.user_filter)
            # if message.data == 'nextstate:changefilterState':
            #     return HelloState(self.chat_id)
        return self
