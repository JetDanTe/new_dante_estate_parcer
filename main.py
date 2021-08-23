from olx_notifier.config import bot

user_states = {}


@bot.message_handler(commands=['start'])
def begin_conversation(message):
    from olx_notifier.states.hello import HelloState
    s = HelloState(message.chat.id)
    s.display()
    user_states[message.chat.id] = s


@bot.callback_query_handler(func=lambda d: True)
def callback_handler(message):
    s = user_states[message.from_user.id]
    s2 = s.proccess(message)
    s2.display()
    user_states[message.from_user.id] = s2


if __name__ == '__main__':
    bot.infinity_polling()
