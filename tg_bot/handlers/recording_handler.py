from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

"""
Функции обработки кнопок списка записей
"""


@rate_limit(2)
async def recording_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Просто отправьте свое имя и номер телефона в чат бота и администратор свяжется с вами!")


def register_recording(dp: Dispatcher):
    dp.register_callback_query_handler(recording_btn, Text(equals='admin_btn'))