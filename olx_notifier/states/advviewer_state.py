from telebot import types

from olx_notifier import olx
from olx_notifier.states.base import BaseState
from olx_notifier.config import bot
from olx_notifier.tg_buttons import SearchButton, ChangeFilterButton


class AdvViewer(BaseState):
    text = ""

    def __init__(self, chat_id):
        super().__init__(chat_id)
        parcer = olx.OlxApi(self.user.settings, self.user.last_viewed)
        bot.send_message(self.chat_id, "Идет поиск, ожидайте, пожалуйста!")
        list_of_advs = parcer.get_adv()
        if len(list_of_advs) <= 5:
            bot.send_message(self.chat_id, "Нет новых объявлений!")
            return

        self.user.last_viewed = list_of_advs[6]['id']
        self.user.save()
        for adv in list_of_advs[6:]:
            adv_formatted = f"{adv['title']}\n{adv['price']}\n{adv['description']}\n{adv['link']}"
            bot.send_message(self.chat_id, adv_formatted, reply_markup=self.keyboard)
        self.keyboard.add(SearchButton.search)
        self.keyboard.add(ChangeFilterButton.change_filter)
        bot.send_message(self.chat_id, "Искать снова?", reply_markup=self.keyboard)

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:searchState':
                return AdvViewer(self.chat_id)
            if message.data == 'nextstate:changefilterState':
                from olx_notifier.states.hello import HelloState
                return HelloState(self.chat_id)
        return self
