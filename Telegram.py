import telebot
from telebot import types
token = 'token'

client = telebot.TeleBot(token)

@client.message_handler(commands=['get_info', 'info'])
def get_users_id(message):
    markup_inline = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='да', callback_data = 'yes')
    button_no = types.InlineKeyboardButton(text='нет', callback_data = 'no')
    markup_inline.add(button_no, button_yes)
    client.send_message(message.chat.id, 'Хотите узнать о себе?',
        reply_markup= markup_inline
    )


@client.callback_query_handler(func=lambda call: True)
def aswer(call):
    if call.data == 'yes':
        markip_a = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_id = types.KeyboardButton(text='МОЙ ID')
        button_users = types.KeyboardButton(text='МОЙ НИК')
        markip_a.add(button_id, button_users)
        client.send_message(call.message.chat.id, 'Нажми на одну из кнопок!',
                            reply_markup=markip_a
                            )
    if call.data == 'no':
        pass
@client.message_handler(content_types=['text'])
def text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your id:{message.from_user.id}')
    if message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your nickname:{message.from_user.first_name} {message.from_user.last_name}')
client.polling(none_stop=True, interval=0)
