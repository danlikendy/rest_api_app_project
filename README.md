# Organizations Directory API

REST API приложение для справочника организаций, зданий и видов деятельности

## Описание

Приложение предоставляет API для управления справочником организаций с поддержкой:
- Организаций с множественными номерами телефонов
- Зданий с географическими координатами
- Иерархических видов деятельности (до 3 уровней вложенности)
- Поиска по различным критериям

## Технологический стек

- **FastAPI** - веб-фреймворк для создания API
- **Pydantic** - валидация данных
- **SQLAlchemy** - ORM для работы с базой данных
- **Alembic** - миграции базы данных
- **PostgreSQL** - база данных
- **Docker** - контейнеризация

## Структура проекта

```
rest_api_app_project/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── models.py      # SQLAlchemy модели
│   │   └── schemas.py     # Pydantic схемы
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py      # Конфигурация
│   └── db/
│       ├── __init__.py
│       └── database.py    # Настройка БД
├── alembic/               # Миграции
├── main.py                # Основное приложение
├── requirements.txt       # Зависимости
├── Dockerfile             # Docker образ
├── docker-compose.yml     # Docker Compose
├── seed_data.py           # Тестовые данные
├── init_db.py             # Инициализация БД
└── README.md              # Документация
```

## Быстрый старт с Docker

### 1. Клонирование и подготовка

```bash
git clone https://github.com/danlikendy/rest_api_app_project
cd rest_api_app_project
```

### 2. Запуск с Docker Compose

```bash
# Запуск всех сервисов
docker-compose up --build

# Или в фоновом режиме
docker-compose up -d --build
```

### 3. Инициализация базы данных

```bash
# Выполнить миграции и заполнить тестовыми данными
docker-compose exec app python init_db.py
```

### 4. Доступ к API

- **API документация (Swagger UI)**: http://localhost:8000/docs
- **API документация (ReDoc)**: http://localhost:8000/redoc
- **API базовый URL**: http://localhost:8000

## Ручная установка (без Docker)

### 1. Установка зависимостей

```bash
# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt
```

### 2. Настройка базы данных

```bash
# Создание базы данных PostgreSQL
createdb organizations_db

# Настройка переменных окружения
export DATABASE_URL="postgresql://user:password@localhost:5432/organizations_db"
export API_KEY="your-secret-api-key-here"
```

### 3. Инициализация

```bash
# Создание миграций и заполнение данными
python init_db.py
```

### 4. Запуск приложения

```bash
# Запуск сервера
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### Аутентификация

Все запросы требуют заголовок `X-API-Key` с секретным ключом.

### Организации

- `GET /organizations` - Список всех организаций
- `GET /organizations/{id}` - Информация об организации по ID
- `GET /organizations/building/{building_id}` - Организации в здании
- `GET /organizations/activity/{activity_id}` - Организации по виду деятельности
- `GET /organizations/search/name?name={name}` - Поиск по названию
- `GET /organizations/search/radius?latitude={lat}&longitude={lng}&radius_km={radius}` - Поиск в радиусе
- `GET /organizations/search/rectangle?min_latitude={min_lat}&max_latitude={max_lat}&min_longitude={min_lng}&max_longitude={max_lng}` - Поиск в прямоугольной области

### Здания

- `GET /buildings` - Список всех зданий
- `GET /buildings/{id}` - Информация о здании по ID

### Виды деятельности

- `GET /activities` - Список всех видов деятельности
- `GET /activities/{id}` - Информация о виде деятельности по ID

## Примеры использования

### Поиск организаций по виду деятельности

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/activity/1"
```

### Поиск организаций в радиусе

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/search/radius?latitude=55.7558&longitude=37.6176&radius_km=5"
```

### Поиск по названию

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/search/name?name=Рога"
```

## Структура данных

### Организация
- `id` - Уникальный идентификатор
- `name` - Название организации
- `building_id` - ID здания
- `phone_numbers` - Список номеров телефонов
- `activities` - Список видов деятельности

### Здание
- `id` - Уникальный идентификатор
- `address` - Адрес
- `latitude` - Широта
- `longitude` - Долгота

### Вид деятельности
- `id` - Уникальный идентификатор
- `name` - Название
- `parent_id` - ID родительского вида деятельности
- `level` - Уровень вложенности (1-3)

## Тестовые данные

Приложение поставляется с тестовыми данными, включающими:
- 5 зданий в Москве
- 4 основных вида деятельности с иерархией до 3 уровней
- 8 организаций с различными видами деятельности

## Остановка сервисов

```bash
# Остановка Docker Compose
docker-compose down

# Остановка с удалением данных
docker-compose down -v
```

## Разработка

### Создание новой миграции

```bash
alembic revision --autogenerate -m "Описание изменений"
alembic upgrade head
```

### Добавление новых тестовых данных

Отредактируйте файл `seed_data.py` и выполните:

```bash
python seed_data.py
```

## Лицензия

MIT License
