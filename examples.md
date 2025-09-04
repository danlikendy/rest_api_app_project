# Примеры использования API

## Настройка

Перед использованием API убедитесь, что:
1. Приложение запущено (`docker-compose up` или `python run.py`)
2. База данных инициализирована (`python init_db.py`)
3. У вас есть API ключ (по умолчанию: `your-secret-api-key-here`)

## Примеры запросов

### 1. Получение списка всех организаций

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations"
```

### 2. Получение информации об организации по ID

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/1"
```

### 3. Поиск организаций в конкретном здании

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/building/1"
```

### 4. Поиск организаций по виду деятельности (с иерархией)

```bash
# Поиск по "Еда" - найдет организации с деятельностью "Еда", "Мясная продукция", "Молочная продукция", "Овощи и фрукты"
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/activity/1"
```

### 5. Поиск организаций по названию

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/search/name?name=Рога"
```

### 6. Поиск организаций в радиусе от точки

```bash
# Поиск в радиусе 5 км от Красной площади
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/search/radius?latitude=55.7539&longitude=37.6208&radius_km=5"
```

### 7. Поиск организаций в прямоугольной области

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/organizations/search/rectangle?min_latitude=55.7&max_latitude=55.8&min_longitude=37.6&max_longitude=37.7"
```

### 8. Получение списка всех зданий

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/buildings"
```

### 9. Получение информации о здании

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/buildings/1"
```

### 10. Получение списка всех видов деятельности

```bash
curl -H "X-API-Key: your-secret-api-key-here" \
     "http://localhost:8000/activities"
```

## Примеры ответов

### Организация

```json
{
  "id": 1,
  "name": "ООО \"Рога и Копыта\"",
  "building_id": 1,
  "phone_numbers": ["2-222-222", "3-333-333", "8-923-666-13-13"],
  "activity_ids": [1, 2],
  "created_at": "2024-01-01T00:00:00",
  "building": {
    "id": 1,
    "address": "г. Москва, ул. Ленина, д. 1, офис 3",
    "latitude": 55.7558,
    "longitude": 37.6176,
    "created_at": "2024-01-01T00:00:00"
  },
  "activities": [
    {
      "id": 1,
      "name": "Еда",
      "parent_id": null,
      "level": 1,
      "created_at": "2024-01-01T00:00:00",
      "children": []
    },
    {
      "id": 2,
      "name": "Мясная продукция",
      "parent_id": 1,
      "level": 2,
      "created_at": "2024-01-01T00:00:00",
      "children": []
    }
  ]
}
```

### Здание

```json
{
  "id": 1,
  "address": "г. Москва, ул. Ленина, д. 1, офис 3",
  "latitude": 55.7558,
  "longitude": 37.6176,
  "created_at": "2024-01-01T00:00:00"
}
```

### Вид деятельности

```json
{
  "id": 1,
  "name": "Еда",
  "parent_id": null,
  "level": 1,
  "created_at": "2024-01-01T00:00:00",
  "children": [
    {
      "id": 2,
      "name": "Мясная продукция",
      "parent_id": 1,
      "level": 2,
      "created_at": "2024-01-01T00:00:00",
      "children": []
    },
    {
      "id": 3,
      "name": "Молочная продукция",
      "parent_id": 1,
      "level": 2,
      "created_at": "2024-01-01T00:00:00",
      "children": []
    }
  ]
}
```

## Тестирование с помощью Python

```python
import requests

API_BASE = "http://localhost:8000"
API_KEY = "your-secret-api-key-here"

headers = {"X-API-Key": API_KEY}

# Получить все организации
response = requests.get(f"{API_BASE}/organizations", headers=headers)
print(response.json())

# Поиск по названию
response = requests.get(f"{API_BASE}/organizations/search/name", 
                       params={"name": "Рога"}, 
                       headers=headers)
print(response.json())
```

## Обработка ошибок

### Неверный API ключ

```json
{
  "detail": "Invalid API key"
}
```

### Организация не найдена

```json
{
  "detail": "Organization not found"
}
```

## Swagger UI

Для интерактивного тестирования API откройте в браузере:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)
