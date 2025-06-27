# USD Rate Project

Проект для отслеживания курса доллара США. 

Для получения курса использован внешний API (https://www.cbr-xml-daily.ru/daily_json.js). 

Между каждым запросом курса установлено временное ограничение 10 секунд с использованием django_ratelimit.decorators import ratelimit.

## Требования

- Python 3.12+
- pip (менеджер пакетов Python)

## Установка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd <Название папки проекта>
```

2. Создайте и активируйте виртуальное окружение:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции базы данных:
```bash
python manage.py migrate
```

## Запуск проекта

1. Запустите сервер разработки:
```bash
python manage.py runserver
```

2. Откройте браузер и перейдите по адресу:
```
http://127.0.0.1:8000/usd/get-current-usd/
```

## Структура проекта

- `usd/` - основное приложение
- `conf/` - конфигурационные файлы
- `manage.py` - скрипт управления Django
- `db.sqlite3` - база данных SQLite
