from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_bot_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать'),
        ],
        [
            KeyboardButton(text='Вычислить производную'),
        ],
        [
            KeyboardButton(text='Вычислить неопределённый интеграл'),
        ],
        [
            KeyboardButton(text='Решить уравнение'),
            KeyboardButton(text='Упростить выражение'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)