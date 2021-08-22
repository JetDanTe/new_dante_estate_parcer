from olx_notifier.config import bot

user_states = {}


# @bot.message_handler(content_types=['text'])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def begin_conversation(message):
    from olx_notifier.states.hello import HelloState
    s = HelloState(message.chat.id)
    s.display()
    user_states[message.chat.id] = s

@bot.callback_query_handler(func=lambda d: True)
def callback_handler(message):
    s = user_states[message.from_user.id]
    print(s)
    s2 = s.proccess(message)
    print(s2)
    s2.display()
    user_states[message.from_user.id] = s2

if __name__ == '__main__':
    bot.infinity_polling()



# @bot.message_handler(commands=['start'])
# def begin_conversation(message):
#     from states.hello import HelloState
#     s = HelloState(message.chat.id)
#     s.display()
#     user_states[message.chat.id] = s
