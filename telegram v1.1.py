# Импортирование модулей
from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.types.input_file import InputFile
import configure

# Создание экземпляра бота
bot = Bot(configure.config['API'])
update = Dispatcher(bot)

# Начальный текст
START_COMMAND = """
Здравствуйте, флешка!
Я бот для ЕГЭ по Информатике.
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
Название задания третьего номера:
Базы данных
Ссылка на сайт: https://labs-org.ru/ege-3/
Перейдя по ссылке можно будет подробно ознакомится с решением данного задания
На фото представлен вид задания
"""
ZADANIE_4 = """
Название задания четвёртого номера
Базы данных
Ссылка на сайт: https://labs-org.ru/ege-4/
Перейдя по ссылке можно будет подробно ознакомится с решением данного задания
На фото представлен вид задания
"""
async def start_command(message: types.Message):
    # Создание клавиатуры
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # Добавление кнопок
    button1 = KeyboardButton('/zadanie')
    button2 = KeyboardButton('/1')
    button3 = KeyboardButton('/2')
    button4 = KeyboardButton('/3')
    button5 = KeyboardButton('/4')
    keyboard.add(button1)
    keyboard.add(button2, button3)
    keyboard.add(button4, button5)
    # Отправка сообщения с клавиатурой
    await bot.send_message(chat_id=message.chat.id, text=START_COMMAND, reply_markup=keyboard)
    await message.delete()


# Определение фукций-обработчиков команд
# async def start_command(message: types.message):
#     """
#     Функция-обработчик команды /start
#     Отправляет приветственное сообщение с инструкцией
#     """
#     await bot.send_message(chat_id=message.chat.id, text=START_COMMAND)
#     await message.delete()

async def zadanie_command(message: types.message):
    """
    Функция-обработчик команды /zadanie
    Отправляет сообщение с инструкцией по выбору задания
    """
    await bot.send_message(chat_id=message.chat.id, text=ZADANIE_TEXT)
    await message.delete()

async def number1_command(call):
    """
    Функция-обработчик команды /1
    Отправляет описание первого задания и прикреплённое к нему изображение
    """
    await bot.send_message(chat_id=call.chat.id, text=ZADANIE_1)
    await bot.send_photo(chat_id=call.chat.id, photo="https://code-enjoy.ru/posts/264/zadanie_1_ege_po_informatike_demoversiya_2022.jpg")
    await call.delete()

async def number2_command(message):
    """
    Функция-обработчик команды /2
    Отправляет описание второго задания и прикреплённое к нему изображение
    """
    await bot.send_message(chat_id=message.chat.id, text=ZADANIE_2)
    #await bot.send_photo(chat_id=message.chat.id) # photo
    await message.delete()

async def number3_command(message):
    """
    Функция-обработчик команды /3
    Отправляет описание третьего задания и прикреплённое к нему изображение
    """
    await bot.send_message(chat_id=message.chat.id, text=ZADANIE_3)
    await bot.send_photo(chat_id=message.chat.id, photo='https://labs-org.ru/wp-content/uploads/2017/06/1_11-28.png')
    await message.delete()

async def number4_command(message):
    """
    Функция-обработчик команды /4
    Отправляет описание четвёртого задания и прикреплённое к нему изображение
    """
    await bot.send_message(chat_id=message.chat.id, text=ZADANIE_4)
    await bot.send_photo(chat_id=message.chat.id, photo='https://code-enjoy.ru/posts/289/ege_po_informatike_2022_zadanie_4_derevo_fano_5.jpg')
    await message.delete()

# Регистрация команд
if __name__ == '__main__':
    print("running...")

    update.register_message_handler(start_command, commands=['start'])
    update.register_message_handler(zadanie_command, commands=['zadanie'])
    update.register_message_handler(number1_command, commands=['1'])
    update.register_message_handler(number2_command, commands=['2'])
    update.register_message_handler(number3_command, commands=['3'])
    update.register_message_handler(number4_command, commands=['4'])

    executor.start_polling(update, skip_updates=False)