from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from config import dp
from keyboards import kb_client, kb_choose_task


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer('Привет. Я бот телеграм для подготовки к ЕГЭ по русскому.' +
                         '\n' + 'Какое задание хочешь отработать?',
                         reply_markup=kb_client)

@dp.message_handler(commands=['Menu'])
async def menu_pressed(message: types.Message):
    await message.answer('Могу в задания:'+'\n'+
                         '№9 - инфа'+'\n'+
                         '№15 - инфа',
                         reply_markup=kb_choose_task)

@dp.message_handler(commands=['Num_9'])
async def num_9_pressed(message: types.Message):
    await message.answer('Вызов задания 9', reply_markup=kb_choose_task)

@dp.message_handler(commands=['Num_15'])
async def num_15_pressed(message: types.Message):
    await message.answer('Вызов задания 15', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(num_9_pressed, commands=['Num_9'])
    dp.register_message_handler(num_15_pressed, commands=['Num_15'])
