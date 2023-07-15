from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from tg_bot.keyboards.callback_data_factory import stocks_callback

stocks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Имплантация Osstem от 1200 рублей в месяц",
                callback_data=stocks_callback.new(
                    stock_name='osstem',
                    stock_date='до 30.07.2023'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text="Брекет-система (США) от 1100 руб/мес",
                callback_data=stocks_callback.new(
                    stock_name='osstem',
                    stock_date='до 30.07.2023'
                )
            )
        ],
        [
            InlineKeyboardButton(
                text="Имплантация all on 4 со скидкой 35%",
                callback_data=stocks_callback.new(
                    stock_name='all-on-4',
                    stock_date='до 30.07.2023'
                )
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