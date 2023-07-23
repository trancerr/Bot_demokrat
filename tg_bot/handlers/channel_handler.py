from aiogram.dispatcher.filters import CommandStart

from tg_bot.keyboards.add_entries_keyboard import online_entries_keyboard
from tg_bot.keyboards.reply import menu
from tg_bot.misc.main_text import text_user_start
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher


@rate_limit(2)
async def user_start_channel(message: types.Message):
    await message.answer(
        f"Привет ",
        reply_markup=online_entries_keyboard
    )


def register_channel_handler(dp: Dispatcher):
    dp.register_channel_post_handler(user_start_channel, CommandStart, content_types=types.ContentTypes.ANY)
