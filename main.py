from aiogram.utils import executor

from data_base import sqlite_db

from config import dp


async def on_startup(_):
    print('Bot started')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
