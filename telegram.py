from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

API = 'token'

bot = Bot(API)
update = Dispatcher(bot)


button_hi = KeyboardButton('Я максимально готов сдать ЕГЭ')
kb1 = ReplyKeyboardMarkup()
kb1.add(button_hi)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

@update.message_handler(commands=['start'])
async def button_hi(message: types.message):
    await message.reply('Здравствуйте,флешка!\nЭтот бот поможет сдать ЕГЭ на 100!!!\nЖду твоего сообщения', reply_markup=kb1)



@update.message_handler(commands=['start'])
async def welcome(message: types.message):
    await message.reply("Здравствуйте,флешка!\nЭтот бот поможет сдать ЕГЭ на 100!!!\nЖду твоего сообщения")

@update.message_handler(commands=['help'])
async def help(message: types.message):
    await  message.reply('Напиши мне что-нибудь и получишь ответ')

@update.message_handler()
async def answer(message: types.message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(update, skip_updates=True)
