from aiogram import types

from config import dp

@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('Йоу, го учиться')