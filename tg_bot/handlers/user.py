from tg_bot.keyboards.reply import menu
from tg_bot.misc.main_text import text_stocks, \
    text_user_start, text_recording, text_story_recording, text_loyalty_program, text_discount
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

'''Функция обработчик кнопки старт'''


@rate_limit(2)
async def user_start(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.first_name},"
        f" {text_user_start}",
        reply_markup=menu
    )


'''Функции обработки кнопок основного меню'''
"""Обработчик кнопки Акции и скидки"""


@rate_limit(2)
async def stocks(message: types.Message):
    await message.answer(text_stocks)


"""Обработчик кнопки ✅Записаться на прием"""


@rate_limit(2)
async def recording(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_recording}")


"""Обработчик кнопки Мои записи"""


@rate_limit(2)
async def story_recording(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_story_recording}")


"""Обработчик кнопки Программа лояльности"""


@rate_limit(2)
async def loyalty_program(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_loyalty_program}")


"""Обработчик кнопки 🤩Скидка 5️% за отзыв о клинике"""
@rate_limit(2)
async def discount(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_discount}")


'''Функция обработчик регистрации hendlers'''


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start', 'help'], state="*")
    dp.register_message_handler(stocks, Text(endswith='скидки'))
    dp.register_message_handler(recording, Text(endswith='прием'))
    dp.register_message_handler(story_recording, Text(endswith='записи'))
    dp.register_message_handler(loyalty_program, Text(endswith='лояльности'))
