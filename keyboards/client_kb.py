from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_menu = KeyboardButton('/Menu')
b_num_9 = KeyboardButton('/Num_9')
b_num_15 = KeyboardButton('/Num_15')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_choose_task = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b_menu)
kb_choose_task.row(b_num_9, b_num_15)