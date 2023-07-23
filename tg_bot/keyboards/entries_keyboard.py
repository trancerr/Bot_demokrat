from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""
Клавиатуры списка записей
"""
not_entries_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🌐Онлайн запись',
                callback_data='online_btn'
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

# list_of_entries_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#
#     ]
# )
