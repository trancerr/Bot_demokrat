from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="💫Акции и скидки"),
        ], 
        [
            KeyboardButton(text="⁉️Остались вопросы..."),
            KeyboardButton(text="✅Записаться на прием")
        ],
        [
            KeyboardButton(text="💎Программа лояльности")
        ],
        [
            KeyboardButton(text="🤩Скидка 5️% за отзыв о клинике")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
