from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="💫Акции и скидки"),
        ], 
        [
            KeyboardButton(text="🧾Мои записи"),
            KeyboardButton(text="✅Записаться на прием")
        ],
        [
            KeyboardButton(text="💎Программа лояльности")
        ],
        [
            KeyboardButton(text="🤩Скидка 5️% за отзыв о клинике")
        ]
    ],
    resize_keyboard=True,
)
