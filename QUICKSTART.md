# Быстрый старт

## Запуск с Docker (рекомендуется)

```bash
# 1. Клонируйте репозиторий
git clone <repository-url>
cd rest_api_app_project

# 2. Запустите все сервисы
docker-compose up --build

# 3. В новом терминале инициализируйте БД
docker-compose exec app python init_db.py

# 4. Откройте API документацию
open http://localhost:8000/docs
```

## Ручной запуск

```bash
# 1. Установите зависимости
pip install -r requirements.txt

# 2. Настройте PostgreSQL и создайте БД
createdb organizations_db

# 3. Установите переменные окружения
export DATABASE_URL="postgresql://user:password@localhost:5432/organizations_db"
export API_KEY="your-secret-api-key-here"

# 4. Инициализируйте БД
python init_db.py

# 5. Запустите приложение
python run.py
```

## Тестирование API

```bash
# Тест с curl
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations"

# Или откройте в браузере
open http://localhost:8000/docs
```

## Остановка

```bash
# Docker
docker-compose down

# Ручной запуск
Ctrl+C
```

## Полезные ссылки

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Примеры использования**: см. examples.md
- **Полная документация**: см. README.md
