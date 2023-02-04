from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
API = 'token'
cd = CallbackData('aaa')
bot = Bot(API)
update = Dispatcher(bot)

button_zadanie = KeyboardButton('/zadanie')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_zadanie)
# Номера заданий
b1 =KeyboardButton('/№1')
b2 =KeyboardButton('/№2')
b3 =KeyboardButton('/№3')
b4 =KeyboardButton('/№4')
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1).add(b2).add(b3).add(b4)

#начальный текст
START_COMMAND = """
Здравствуйте, флешка!
Я бот для ЕГЭ по Информатики.
Я помогу сдать тебе ЕГЭ на 💯!!!
Для начало работы нажми на кнопку задания.
Данный бот создан в целях научить вас информатике, а не найти ответ на задачу😁😄😉
"""
ZADANIE_TEXT = """
Нажми на кнопку с соответствующим заданием.
"""
ZADANIE_1 = """
    Название задания первого номера:
Структурирование информации и информационные модели
Ссылка на сайт: https://labs-org.ru/ege-1/
Перейдя по ссылке можно будет подробно ознакомиться с решением данного задания
На фото представлен вид задания
"""
@update.message_handler(commands=['start'])
async def welcome(message: types.message):
    await bot.send_message(chat_id=message.chat.id,
                           text=START_COMMAND,
                        reply_markup=kb
                           )
    await message.delete()

@update.message_handler(commands=['zadanie'])
async def zadanie(message: types.message):
    await bot.send_message(chat_id=message.chat.id,
                           text=ZADANIE_TEXT,
                        reply_markup=kb1
                           )
    await message.delete()
@update.message_handler(commands=['№1'])
async def numer1(call):
    await bot.send_photo(chat_id=call.chat.id,
                         photo="https://labs-org.ru/wp-content/uploads/2017/06/1-85.png"
                             )
    await bot.send_message(chat_id=call.chat.id,
                           text=ZADANIE_1
                           )
    await call.delete()

if __name__ == '__main__':
    executor.start_polling(update, skip_updates=True)