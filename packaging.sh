#!/bin/bash

venv/bin/pip freeze > requirements.txt

# Запрашиваем коммитить изменения
read -p "Введите текст коммита: " commit_message

echo $commit_message

git add .

git commit -m "$commit_message"

git push https://github.com/thebbstudio/ССЫЛКА_НА_РЕПОЗИТОРИЙ.git

echo 'Проект собран'