# EGE Bot Trainer

### English version:


EGE Bot Trainer is a Telegram chatbot designed to help users practice solving problems from the Russian language section of the Unified State Exam (EGE). The bot currently supports solving problems for types 8, 9, 11, 12, 13, 14, and 15, and more types of test problems are planned to be added in the future.


## Getting started
### For users

Open the bot in Telegram by finding it at https://t.me/RU_EGE_bot and type `/start` to begin.

### For developers
#### If you want to run a bot on your machine
1. Clone the repository and install Python 3.10 and aiogram.
2. Create a Telegram bot and get the token.
3. Create a `.bat` file with the following code:

```
@echo off

call <Project Path>\venv\Scripts\activate

cd <Project Path>

set TOKEN=<bot token>
set PASSWORD=<your password>

python <Launch File>

pause
```

4. Replace `<Project Path>`, `<bot token>`, `<your password>`, and `<Launch File>` with the correct paths and names.
5. Run the `.bat` file to start the bot.

## Usage

The bot supports the following commands:

### For users
- `/start` - Start the bot and see the list of available commands.
- `/problem_solving` - Start solving EGE tasks.
- `/quit` - Quit the task-solving loop.

### For developers
- `/admin` - Login to administrator mode. The bot will require the password that was specified in the .bat file.
- `/add_problem` - Start entering the task into the database.
- `/check_database` - Check the tasks in the database.
- `/quit` - Exit admin mode.

## Database

The SQLite database is automatically created by the sqlite_db.py file. The database contains all tasks and is included in the repository. In the future, we plan to add a user statistics database, but it will not be uploaded to the repository.

## Future Plans

We plan to add the following features in the future:

- Add more tasks to the database.
- Allow users to view their statistics.
- Add more optimized tasks to speed up the learning process.

## Contact

For any questions or feedback, please contact damir.ernazarov.yesspeace@gmail.com.

# EGE Bot Trainer

### Версия на русском:


EGE Bot Trainer - это чат-бот в Telegram, созданный для помощи пользователям в решении задач по русскому языку в разделе Единого Государственного Экзамена (ЕГЭ). Бот в настоящее время поддерживает решение задач для типов 8, 9, 11, 12, 13, 14 и 15, и в будущем планируется добавление новых типов тестовых заданий.

## Начало работы
### Для пользователей

Откройте бот в Telegram, найдя его по ссылке https://t.me/RU_EGE_bot, и наберите команду /start, чтобы начать.

### Для разработчиков
#### Если вы хотите запустить бота на своей машине
1. Клонируйте репозиторий и установите Python 3.10 и aiogram.
2. Создайте бота в Telegram и получите токен.
3. Создайте файл .bat со следующим кодом:

```
@echo off

call <Project Path>\venv\Scripts\activate

cd <Project Path>

set TOKEN=<bot token>
set PASSWORD=<your password>

python <Launch File>

pause
```

4. Замените <Project Path>, <bot token>, <your password> и <Launch File> на соответствующие пути и имена файлов.
5. Запустите файл .bat, чтобы запустить бота.

## Использование

Бот поддерживает следующие команды:

### Для пользователей
- `/start` - Запустить бота и увидеть список доступных команд.
- `/problem_solving` - Начать решение задач ЕГЭ.
- `/quit` - Выход из цикла решения задач.

### Для разработчиков
- `/admin` - Войти в режим администратора. Бот потребует пароль, указанный в файле .bat.
- `/add_problem` - Начать ввод задачи в базу данных.
- `/check_database` - Проверить задачи в базе данных.
- `/quit` - Выйти из режима администратора.

## База данных

База данных SQLite автоматически создается файлом sqlite_db.py. База данных содержит все задачи и включена в репозиторий. В будущем мы планируем добавить базу данных статистики пользователей, но она не будет загружаться в репозиторий.

## Планы на будущее

Мы планируем добавить следующее в будущем:

- Добавить больше задач в базу данных.
- Позволить пользователям просматривать свою статистику.
- Добавить более оптимизированные задачи для ускорения процесса обучения.

## Контакты

По любым вопросам или отзывам обращайтесь по почте - damir.ernazarov.yesspeace@gmail.com.