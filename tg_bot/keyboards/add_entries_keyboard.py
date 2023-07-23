from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

"""
Клавиатура записи
"""
online_entries_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🌐Онлайн запись',
                callback_data='online_btn'
            )
        ],
[
            InlineKeyboardButton(
                text='📝Запись через администратора',
                callback_data='admin_btn'
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

add_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='📱Поделится номером',
                request_contact=True
            )
        ],
        [
            KeyboardButton(
                text='↩️На главное меню',
            )
        ],
    ],
    resize_keyboard=True
)