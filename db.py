import aiosqlite
from config import DB_NAME
import os



# Получение пути до проекта
project_path = os.path.dirname(os.path.abspath(__file__))
# Получение пути до папки db в проекте
db_path = os.path.join(project_path, 'db')
# Создание папки db, если ее нет
if not os.path.exists(db_path):
    os.makedirs(db_path)
# Путь до файла базы данных
db_file = os.path.join(db_path, DB_NAME)


async def init_db():
    async with aiosqlite.connect(db_file) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS parasitic_words
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT)''')
        await db.commit()
        

async def add_word(word):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('INSERT INTO parasitic_words (word) VALUES (?)', (word,))
        await db.commit()


async def list_words():
    async with aiosqlite.connect(db_file) as db:
            async with db.execute('SELECT word FROM parasitic_words') as cursor:
                return await cursor.fetchall()