from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

"""
Клавиатура отзыва о клинике
"""
review_clinic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='💬Оставить отзыв',
                web_app=WebAppInfo(url='https://clck.ru/353Joo')
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
