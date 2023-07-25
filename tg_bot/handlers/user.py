from tg_bot.keyboards.add_entries_keyboard import online_entries_keyboard
from tg_bot.keyboards.entries_keyboard import not_entries_keyboard
from tg_bot.keyboards.inline import stocks_keyboard
from tg_bot.keyboards.loyalty_program_keyboard import loyalty_keyboard
from tg_bot.keyboards.reply import menu
from tg_bot.keyboards.review_keyboard import review_clinic_keyboard
from tg_bot.keyboards.suppot_keyboard import support_chat_keyboard
from tg_bot.misc.main_text import text_stocks, \
    text_user_start, text_recording, text_story_recording, text_loyalty_program, text_discount, text_user_help, \
    text_support_chat
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

'''Функция обработчик кнопки старт'''


@rate_limit(2)
async def user_start(message: types.Message):
    sticer_id = 'CAACAgIAAxkBAAEJxbhku52mDv5Cx65n7L16iWT6LRUoXgACijQAAqJ22ElFrNpdiXThvS8E'
    await message.answer_sticker(sticker=sticer_id, reply_markup=menu)
    await message.answer(f"Привет {message.from_user.first_name},"
                         f" {text_user_start}",
                         reply_markup=menu)


@rate_limit(2)
async def user_help(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name},"
                         f" {text_user_help}",
                         reply_markup=menu)


'''Функции обработки кнопок основного меню'''
"""Обработчик кнопки Акции и скидки"""


@rate_limit(2)
async def stocks(message: types.Message):
    await message.answer(text_stocks, reply_markup=stocks_keyboard)


"""Обработчик кнопки ✅Записаться на прием"""


@rate_limit(2)
async def recording(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_recording}", reply_markup=online_entries_keyboard)


"""Обработчик кнопки Мои записи"""


# @rate_limit(2)
# async def story_recording(message: types.Message):
#     await message.answer(f"{message.from_user.first_name}\n"
#                          f"{text_story_recording}", reply_markup=not_entries_keyboard)

@rate_limit(2)
async def support_chat(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_support_chat}", reply_markup=support_chat_keyboard)


"""Обработчик кнопки Программа лояльности"""


@rate_limit(2)
async def loyalty_program(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_loyalty_program}", reply_markup=loyalty_keyboard)


"""Обработчик кнопки 🤩Скидка 5️% за отзыв о клинике"""


@rate_limit(2)
async def review_clinic(message: types.Message):
    await message.answer(f"{message.from_user.first_name}\n"
                         f"{text_discount}", reply_markup=review_clinic_keyboard)


'''Функция обработчик регистрации hendlers'''


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'],
                                state="*")
    dp.register_message_handler(user_help, commands=['help'], state='*')
    dp.register_message_handler(stocks, Text(endswith='скидки'))
    dp.register_message_handler(recording, Text(endswith='прием'))
    # dp.register_message_handler(story_recording, Text(endswith='записи'))
    dp.register_message_handler(support_chat, Text(endswith='...'))
    dp.register_message_handler(loyalty_program, Text(endswith='лояльности'))
    dp.register_message_handler(review_clinic, Text(contains='отзыв'))
