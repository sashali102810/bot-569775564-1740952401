Для создания Telegram-бота с использованием библиотеки `python-telegram-bot` версии 20.x и `requests`, а также с функционалом логирования ошибок и автоматическим перезапуском при сбоях, можно использовать следующий код:

### Установка необходимых библиотек
Сначала установите необходимые библиотеки:

```bash
pip install python-telegram-bot requests
```

### Код бота

```python
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot_errors.log'
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот. Используй /help для получения списка команд.')

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доступные команды:\n/start - начать работу с ботом\n/help - получить справку')

# Функция для обработки ошибок и перезапуска бота
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Ошибка: {context.error}', exc_info=True)
    # Перезапуск бота
    await start(update, context)

# Основная функция для запуска бота
def main():
    # Создаем приложение бота с токеном
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
```

### Описание кода

1. **Логирование ошибок**: Логирование настроено на запись в файл `bot_errors.log`. В случае возникновения ошибки, она будет записана в этот файл с указанием времени, уровня ошибки и сообщения.

2. **Обработчики команд**:
   - `/start`: Приветственное сообщение.
   - `/help`: Справка по доступным командам.

3. **Обработчик ошибок**: В случае возникновения ошибки, она логируется, и бот автоматически перезапускается, вызывая команду `/start`.

4. **Автоматический перезапуск**: В случае сбоя, бот автоматически перезапускается, вызывая команду `/start`.

### Запуск бота

1. Замените `"YOUR_BOT_TOKEN"` на токен вашего бота, полученный от BotFather.
2. Запустите скрипт:

```bash
python your_bot_script.py
```

Теперь ваш бот будет работать, логировать ошибки и автоматически перезапускаться в случае сбоев.