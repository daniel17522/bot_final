from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)
start_buttons = KeyboardButton('/start')

info_buttons = KeyboardButton('/info')

start.add(info_buttons, start_buttons)
