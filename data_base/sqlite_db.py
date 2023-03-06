import json
import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('problem_base.db')
    cur = base.cursor()
    if base:
        print('Date base connected OK')

    for num in [8, 9, 11, 12, 13, 14, 15]:

        base.execute(
            f'CREATE TABLE IF NOT EXISTS problem_type_{num} (id INTEGER PRIMARY KEY AUTOINCREMENT, problem TEXT, solution TEXT, '
            'type TEXT)'
        )

    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        solution = json.dumps(data['solution'])

        cur.execute(f'INSERT INTO {data["type"]} (type, problem, solution) VALUES (?, ?, ?)',
                    (data['type'], data['problem'], solution))

        base.commit()


async def sql_read(bot, callback_query, type):
    for row in cur.execute(f'SELECT * FROM {type}').fetchall():
        row = list(row)
        row[2] = json.loads(row[2])
        row = tuple(row)

        await bot.send_message(
            callback_query.from_user.id,
            text=f'Тип задачи: {type} \n' +
            '\n' +
            f'id задачи: {row[0]} \n' +
            '\n' +
            'Задача:\n' +
            f'{row[1]}\n' +
            '\n'
            'Ответ:\n' +
            f'{row[2]}')
