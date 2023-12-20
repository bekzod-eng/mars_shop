from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


new_bot= ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="1"),
        KeyboardButton(text="2")
        ],
        [
        KeyboardButton(text="3"),
        KeyboardButton(text="4")
        ],
    ], resize_keyboard=True
    )