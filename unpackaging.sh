#!/bin/bash

# Получаем изменения из Git-репозитория
git pull https://github.com/thebbstudio/habr-bot.git

# Проверяем наличие файла config.py
if [ ! -f "config.py" ]; then
    # Запрашиваем ввод значений для создания файла config.py
    read -p "Введите значение для переменной TG_TOKEN: " value_1
    read -p "Введите значение для переменной DB_NAME: " value_2

    # Создаем файл config.py и записываем в него значения
    echo "TG_TOKEN=\"$value_1\"" > config.py
    echo "DB_NAME=\"$value_2\"" >> config.py
fi