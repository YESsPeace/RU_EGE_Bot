from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b_add = KeyboardButton('/add_problem')
b_delete = KeyboardButton('/delete_problem')
b_check = KeyboardButton('/check_database')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.add(b_add).add(b_delete).add(b_check)

add_db_choose_type_kb = InlineKeyboardMarkup()

check_db_choose_type_kb = InlineKeyboardMarkup()

button_type_8 = InlineKeyboardButton(text='Тип 8', callback_data='add_db_type_8')
button_type_9 = InlineKeyboardButton(text='Тип 9', callback_data='add_db_type_9')
button_type_11 = InlineKeyboardButton(text='Тип 11', callback_data='add_db_type_11')
button_type_12 = InlineKeyboardButton(text='Тип 12', callback_data='add_db_type_12')
button_type_13 = InlineKeyboardButton(text='Тип 13', callback_data='add_db_type_13')
button_type_14 = InlineKeyboardButton(text='Тип 14', callback_data='add_db_type_14')
button_type_15 = InlineKeyboardButton(text='Тип 15', callback_data='add_db_type_15')

add_db_choose_type_kb.insert(button_type_8).insert(button_type_9).insert(button_type_11).insert(button_type_12)
add_db_choose_type_kb.insert(button_type_13).insert(button_type_14).insert(button_type_15)

button_type_8 = InlineKeyboardButton(text='Тип 8', callback_data='check_db_type_8')
button_type_9 = InlineKeyboardButton(text='Тип 9', callback_data='check_db_type_9')
button_type_11 = InlineKeyboardButton(text='Тип 11', callback_data='check_db_type_11')
button_type_12 = InlineKeyboardButton(text='Тип 12', callback_data='check_db_type_12')
button_type_13 = InlineKeyboardButton(text='Тип 13', callback_data='check_db_type_13')
button_type_14 = InlineKeyboardButton(text='Тип 14', callback_data='check_db_type_14')
button_type_15 = InlineKeyboardButton(text='Тип 15', callback_data='check_db_type_15')

check_db_choose_type_kb.insert(button_type_8).insert(button_type_9).insert(button_type_11).insert(button_type_12)
check_db_choose_type_kb.insert(button_type_13).insert(button_type_14).insert(button_type_15)