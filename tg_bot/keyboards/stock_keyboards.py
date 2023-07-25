from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

"""
Клавиатуры акций
"""
osstem_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Подробнее об акции',
                web_app=WebAppInfo(url='https://demokrat-nn.ru/stocks')

            )
        ],
        [
            InlineKeyboardButton(
                text='🌐Записаться по акции',
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

brecket_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Подробнее об акции',
                web_app=WebAppInfo(url='https://demokrat-nn.ru/stocks')
            )
        ],
        [
            InlineKeyboardButton(
                text='🌐Записаться по акции',
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

all_on_4_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Подробнее об акции',
                web_app=WebAppInfo(url='https://demokrat-nn.ru/stocks')
            )
        ],
        [
            InlineKeyboardButton(
                text='🌐Записаться по акции',
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
