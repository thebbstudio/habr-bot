# Используем базовый образ Python
FROM python:3.12.3

# Устанавливаем переменную окружения для отключения записи .pyc файлов
ENV PYTHONDONTWRITEBYTECODE 1

# Устанавливаем переменную окружения для вывода сообщений ошибок в stdout
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем содержимое текущей директории в контейнер в /app
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
