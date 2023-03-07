from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import dp, password, bot

from data_base import sql_read, sql_add_command
from keyboards import kb_admin, add_db_choose_type_kb, check_db_choose_type_kb


class FSMAdmin(StatesGroup):
    waiting_for_password = State()
    admin = State()
    problem = State()
    solution = State()


# exit from state to admin state
@dp.message_handler(commands='cancel', state='*')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if not (current_state is None):
        await state.finish()
        await FSMAdmin.admin.set()
        await message.answer('Отмена. Состояние - админ')


# exit from admin state
@dp.message_handler(commands='quit', state=FSMAdmin.admin)
@dp.message_handler(Text(equals='quit', ignore_case=True), state=FSMAdmin.admin)
async def quit_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Выход из состояния админа.\n' +
                         'Состояние - пользователь')


# entry into admin state
@dp.message_handler(commands=['admin'], state=None)
async def process_secret_command(message: types.Message):
    # ask to input the password
    await message.answer('Введите пароль для доступа к секретному функционалу:')

    # new state 'waiting_for_password'
    await FSMAdmin.waiting_for_password.set()


# checking password
@dp.message_handler(state=FSMAdmin.waiting_for_password)
async def process_admin_password(message: types.Message):
    if message.text == password:
        await message.answer('Вы успешно вошли в секретный режим.',
                             reply_markup=kb_admin)
        await FSMAdmin.admin.set()
    else:
        await message.reply('Неверный пароль. Попробуйте еще раз:')


# add a new problem
@dp.message_handler(commands=['add_problem'], state=FSMAdmin.admin)
async def load_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = 'choosing'

    await message.answer('Выберите тип задачи:', reply_markup=add_db_choose_type_kb)


# callback func if button call any 'type_' like 'type_15'
@dp.callback_query_handler(lambda c: c.data.startswith('add_db_type_'), state=FSMAdmin.admin)
async def process_callback_type(callback_query: types.CallbackQuery, state: FSMContext):
    selected_type = callback_query.data.split('_')[-1]  # get button call data

    await bot.answer_callback_query(callback_query.id, text=f'Выбран тип задачи {selected_type}')

    await bot.send_message(callback_query.from_user.id, text=f'Выбран тип задачи {selected_type}')

    async with state.proxy() as data:
        data['type'] = 'problem_type_' + selected_type

        await get_problem_text(callback_query)


@dp.callback_query_handler(lambda c: c.data.startswith('check_db_type_'), state=FSMAdmin.admin)
async def process_callback_type(callback_query: types.CallbackQuery):
    selected_type = callback_query.data.split('_')[-1]  # get button call data

    await sql_read(bot, callback_query, type='problem_type_' + selected_type)

    await FSMAdmin.admin.set()


async def get_problem_text(callback_query):
    await bot.send_message(callback_query.from_user.id, text='Введите текст задания.\n\n' +
                                                             '/cancel - для выхода')
    await FSMAdmin.problem.set()


@dp.message_handler(state=FSMAdmin.problem)
async def load_problem(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['problem'] = message.text
    await FSMAdmin.next()
    await message.answer('Введите ответ к заданию.\n\n' +
                         '/cancel - для выхода')


@dp.message_handler(state=FSMAdmin.solution)
async def load_solution(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if 'solution' not in data:
            data['solution'] = []

        if message.text == '/done':
            await add_to_database(message, state)

            await FSMAdmin.admin.set()

            await message.answer('Выберите новый тип задачи:', reply_markup=add_db_choose_type_kb)

            return

        data['solution'].append(message.text)

    await message.answer('Если есть ещё один вариант ответа, то введите его.\n\n' +
                         'Если - нет, то введите /done')


@dp.message_handler(Text(equals='/done'), state=FSMAdmin.solution)
async def add_to_database(message: types.Message, state: FSMContext):
    await sql_add_command(state)

    async with state.proxy() as data:
        await message.answer(
            'Задача записана.\n' +
            f'Тип задачи: Тип {data["type"].split("_")[-1]}' +
            '\n' +
            'Задача:\n' +
            f'{data["problem"]}\n' +
            '\n' +
            'Ответ:\n' +
            f'{data["solution"]}'
        )

    await state.finish()
    await FSMAdmin.admin.set()


@dp.message_handler(commands=['check_database'], state=FSMAdmin.admin)
async def database_read(message: types.Message):
    await message.answer('Выберите тип задачи:', reply_markup=check_db_choose_type_kb)


def register_handlers_admin(dp: Dispatcher):
    dp.register_callback_query_handler(process_callback_type, lambda c: c.data.startswith('type_'),
                                       state=FSMAdmin.admin)

    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(cancel_handler, state="*", commands='quit')
    dp.register_message_handler(cancel_handler, Text(equals='quit', ignore_case=True), state='*')

    dp.register_message_handler(process_secret_command, commands=['admin'], state=None)
    dp.register_message_handler(process_admin_password, state=FSMAdmin.waiting_for_password)

    dp.register_message_handler(add_to_database, (Text(equals='/done')), state=FSMAdmin.solution)
    dp.register_message_handler(load_problem, state=FSMAdmin.problem)
    dp.register_message_handler(load_solution, state=FSMAdmin.solution)

    dp.register_message_handler(database_read, commands=['check_database'], state=FSMAdmin.admin)
