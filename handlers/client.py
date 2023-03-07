from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from config import dp, bot
from keyboards import kb_client, choose_problem_type_kb

from data_base import select_random_problem


class FSMClient(StatesGroup):
    solution = State()


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer('Привет. Я бот телеграм для подготовки к ЕГЭ по русскому.\n' +
                         'Xочешь отработать какое-нибудь задание?\n' +
                         'Тогда нажми /Problem_solving',
                         reply_markup=kb_client)


@dp.message_handler(commands=['quit'], state=FSMClient.solution)
@dp.message_handler(Text(equals='quit', ignore_case=True), state=FSMClient.solution)
async def command_quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Вы хорошо постарались, решив {len(used_problems) - 1} задачи. Пока')


@dp.message_handler(commands=['Problem_solving'])
async def problem_solving(message: types.Message):
    global used_problems

    await message.answer('Выбирите тип задания:',
                         reply_markup=choose_problem_type_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('solving_type_'))
async def choose_problem_type(callback_query: types.CallbackQuery):
    global problem_dict, used_problems

    problem_type = callback_query.data.split('_')[-1]

    problem_dict, max_number_of_problems = await select_random_problem(problem_type)

    used_problems = [problem_dict]

    await bot.send_message(
        callback_query.from_user.id,
        text=
        f'{problem_dict["problem_text"]}\n\n'
        'А теперь введите ответ\n\n'
        '/quit - для выхода'
    )

    await FSMClient.solution.set()


@dp.message_handler(state=FSMClient.solution)
async def load_solution(message: types.Message, state: FSMContext):
    global problem_dict

    if message.text in problem_dict['solution']:
        await message.answer('✅ Правильно')

        problem_dict, max_number_of_problems = await select_random_problem(problem_dict['type'])

        if len(used_problems) >= max_number_of_problems:

            await message.answer(
                'Блин, задачи такого типа закончились\n' +
                f'Кста, вы решили {len(used_problems)} задачи такого типа'
            )

            await message.answer('Выбирите новый тип задания:',
                                 reply_markup=choose_problem_type_kb)

            await state.finish()

        else:

            while problem_dict in used_problems:
                problem_dict, max_number_of_problems = await select_random_problem(problem_dict['type'])

            used_problems.append(problem_dict)

            await message.answer(
                f'{problem_dict["problem_text"]}\n\n'
                'А теперь введите ответ\n\n'
                '/quit - для выхода'
            )

    else:
        await message.answer('❌ Попробуйте ещё')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(problem_solving, commands=['Problem_solving'])
