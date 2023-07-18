from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
                text="В начало",
                callback_data='cancel'
            )
        ],
    ]
)