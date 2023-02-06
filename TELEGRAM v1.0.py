import configure
from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import InputFile

bot = Bot(configure.config['API'])
update = Dispatcher(bot)

#button_zadanie = KeyboardButton('/zadanie')
#kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_zadanie)
# Номера заданий
#b1 =KeyboardButton('/№1')
#b2 =KeyboardButton('/№2')
#b3 =KeyboardButton('/№3')
#b4 =KeyboardButton('/№4')
#kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1).add(b2).add(b3).add(b4)


#начальный текст
START_COMMAND = """
Здравствуйте, флешка!
Я бот для ЕГЭ по Информатики.
Я помогу сдать тебе ЕГЭ на 💯!!!
Для начало работы нажми на кнопку задания.
Данный бот создан в целях научить вас информатики, а не найти ответ на задачу😁😄😉
"""
ZADANIE_TEXT = """
Нажми на кнопку с соответствующим заданием.
"""
ZADANIE_1 = """
    Название задания первого номера:
Структурирование информации и информационные модели
Ссылка на сайт: https://labs-org.ru/ege-1/
Перейдя по ссылке можно будет подробно ознакомится с решением данного задания
На фото представлен вид задания
"""
ZADANIE_2 = """
    Название задания второго номера:
Построение таблиц истинности логических выражений 
На фото представлена программа для решения данного задания.
"""
ZADANIE_3 = """
    Название задания первого номера:
                Базы данных
Ссылка на сайт: https://labs-org.ru/ege-3/
Перейдя по ссылке можно будет подробно ознакомится с решением данного задания
На фото представлен вид задания
"""
ZADANIE_4 = """
    Название задания первого номера:
                Базы данных
Ссылка на сайт: https://labs-org.ru/ege-4/
Перейдя по ссылке можно будет подробно ознакомится с решением данного задания
На фото представлен вид задания
"""
photo=InputFile('/home/dmitrii/Документы/telegram_bot/venv/zadanie2.png')
@update.message_handler(commands=['start'])
async def welcome(message: types.message):
    await bot.send_message(chat_id=message.chat.id,
                           text=START_COMMAND
                           )
    await message.delete()

@update.message_handler(commands=['zadanie'])
async def zadanie(message: types.message):
    await bot.send_message(chat_id=message.chat.id,
                           text=ZADANIE_TEXT,
                           )
    await message.delete()

@update.message_handler(commands=['1'])
async def numer1(call):
    await bot.send_message(chat_id=call.chat.id,
                           text=ZADANIE_1
                           )
    await bot.send_photo(chat_id=call.chat.id,
                         photo="https://code-enjoy.ru/posts/264/zadanie_1_ege_po_informatike_demoversiya_2022.jpg"
                         )
    await call.delete()

@update.message_handler(commands=['2'])
async def numer2(message):
    await bot.send_message(chat_id=message.chat.id,
                           text=ZADANIE_2
                           )
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo
                         )
    await message.delete()
@update.message_handler(commands=['3'])
async def numer2(message):
    await bot.send_message(chat_id=message.chat.id,
                           text=ZADANIE_3
                           )
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://labs-org.ru/wp-content/uploads/2017/06/1_11-28.png'
                         )
    await message.delete()
@update.message_handler(commands=['4'])
async def numer2(message):
    await bot.send_message(chat_id=message.chat.id,
                           text=ZADANIE_4
                           )
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://code-enjoy.ru/posts/289/ege_po_informatike_2022_zadanie_4_derevo_fano_5.jpg'
                         )
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(update, skip_updates=True)