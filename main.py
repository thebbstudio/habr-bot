import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
from db import init_db, list_words, add_word
from config import TG_TOKEN



# Initialize bot and dispatcher
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()


# Handler for /start command
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Привет! Этот бот записывает слова-паразиты в базу данных.")
    await init_db()


# Handler for adding parasitic words
@dp.message(Command('add'))
async def add_parasitic_word(message: types.Message):
    words = message.text.split('/add ')
    if len(words) == 1:
        await message.reply("Вы не ввели слово для добавления в базу данных.")
        return

    word = ' '.join(words[1:])
    await add_word(word)
    await message.reply(f"Слово '{word}' успешно добавлено в базу данных!")


# Handler for displaying all parasitic words
@dp.message(Command('list'))
async def list_parasitic_words(message: types.Message):
    words = await list_words()
    if words:
        word_list = "\n".join( ' - ' + word[0] for word in words)
        await message.reply(f"Список слов-паразитов в базе данных:\n{word_list}")
    else:
        await message.reply("В базе данных нет записей о словах-паразитах.")

# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

# Start the bot
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
