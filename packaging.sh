#!/bin/bash

venv/bin/pip freeze > requirements.txt

# Проверяем наличие непроиндексированных изменений
if ! git diff --quiet; then
    echo "Есть непроиндексированные изменения. Пожалуйста, закоммитьте или отмените их перед продолжением."
    git status
    exit 1
fi


# Запрашиваем коммитить изменения
read -p "Введите текст коммита: " commit_message

echo $commit_message

git add .

git commit -m "$commit_message"

echo 'Проект собран'