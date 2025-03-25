# Task Management API

Простое FastAPI-приложение для управления задачами с хранением в памяти.

## Функционал
- Добавление задач с названием, описанием и дедлайном
- Просмотр списка задач с сортировкой по дедлайну
- Удаление задач по ID

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий.git
   cd task-management-api
2. Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
3. Установите зависимости:
pip install -r requirements.txt
4. Запуск
python app.py

## Документация API
Swagger UI: http://127.0.0.1:8000/docs
##  Примеры запросов
# Создание задачи
curl -X POST "http://localhost:8000/tasks" \
-H "Content-Type: application/json" \
-d '{"title":"Купить молоко","description":"Пойти в магазин","deadline":"20-03-2025"}'

# Получение списка задач
curl "http://localhost:8000/tasks"

# Удаление задачи
curl -X DELETE "http://localhost:8000/tasks/1"
##  Тестирование
pytest test_app.py -v
