from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_stop = KeyboardButton('/stop_game')
btn_restart = KeyboardButton('/new_game')
btn_start = KeyboardButton('/start')

kb.add(btn_stop, btn_restart)
kb_start.add(btn_start)
