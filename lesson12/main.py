import telebot as tb

from lesson12.config import TOKEN

bot = tb.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Hi!")

#
# @bot.message_handler(func=lambda message: True)
# def message(message):
#     bot.send_message(message.chat.id, "Oh No!")


@bot.message_handler(func=lambda m: m.text == 'keyboard')
def keyboard_example(message):
    message_kb = tb.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    message_kb.row('1', '2', '3')
    message_kb.row('4', '5', '6')
    bot.send_message(message.chat.id,
                     'keyboard_example',
                     reply_markup=message_kb)


@bot.callback_query_handler(func=lambda call: call.data)
def callback_example(message):
    inline_kb = tb.types.InlineKeyboardMarkup()
    button_kb = [tb.types.InlineKeyboardButton(text=f'text_{i}', callback_data=str(i))
                 for i in range(21)]
    inline_kb.add(*button_kb)
    bot.send_message(message.chat.id,
                     'Inline message',
                     reply_markup=inline_kb)


if __name__ == '__main__':
    bot.polling()
