from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b_start = KeyboardButton('/Problem_solving')

button_type_8 = InlineKeyboardButton(text='Тип 8', callback_data='solving_type_8')
button_type_9 = InlineKeyboardButton(text='Тип 9', callback_data='solving_type_9')
button_type_11 = InlineKeyboardButton(text='Тип 11', callback_data='solving_type_11')
button_type_12 = InlineKeyboardButton(text='Тип 12', callback_data='solving_type_12')
button_type_13 = InlineKeyboardButton(text='Тип 13', callback_data='solving_type_13')
button_type_14 = InlineKeyboardButton(text='Тип 14', callback_data='solving_type_14')
button_type_15 = InlineKeyboardButton(text='Тип 15', callback_data='solving_type_15')

choose_problem_type_kb = InlineKeyboardMarkup(resize_keyboard=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

choose_problem_type_kb.insert(button_type_8).insert(button_type_9).insert(button_type_11).insert(button_type_12)
choose_problem_type_kb.insert(button_type_13).insert(button_type_14).insert(button_type_15)

kb_client.add(b_start)
