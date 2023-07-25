from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

support_chat_keyboard = InlineKeyboardMarkup(
    items=[
        [
            InlineKeyboardButton(
                text="Связаться с администратором",
                сhild_button='support_chat'
            )
        ],
        [
            InlineKeyboardButton(
                text="F.A.Q",
                callback_data='f_a_q'
            )
        ],
        [
            InlineKeyboardButton(
                text="↩️На главное меню",
                callback_data='cancel'
            )
        ],

    ]
)