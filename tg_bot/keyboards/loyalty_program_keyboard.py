from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""
Клавиатура программы лояльности
"""
loyalty_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="↩️На главное меню",
                callback_data='cancel'
            )
        ],
    ]
)