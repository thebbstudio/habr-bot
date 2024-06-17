#!/bin/bash

venv/bin/pip freeze > requirements.txt

# Запрашиваем коммитить изменения
read -p "Введите текст коммита: " commit_message

echo $commit_message

git add .

git commit -m "$commit_message"

git push

echo 'Проект собран'