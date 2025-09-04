# Organizations Directory API

REST API для справочника организаций с поддержкой зданий и видов деятельности

## Описание

Приложение предоставляет API для работы с:
- **Организации** - название, телефоны, здание, виды деятельности
- **Здания** - адрес, географические координаты
- **Виды деятельности** - иерархическая структура (до 3 уровней)

## Быстрый старт

### 1. Запуск сервера
```bash
python3 simple_app.py
```

### 2. Открыть интерфейс
Откройте `advanced_test.html` в браузере для тестирования API

## API Endpoints

**Base URL:** `http://localhost:8000` (или ваш IP)  
**API Key:** `api-key`

### Организации

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/organizations` | Все организации |
| GET | `/organizations/{id}` | Организация по ID |
| GET | `/organizations/search/name?name={name}` | Поиск по названию |
| GET | `/organizations/building/{building_id}` | Организации в здании |
| GET | `/organizations/activity/{activity_id}` | Организации по виду деятельности |
| GET | `/organizations/search/radius?latitude={lat}&longitude={lng}&radius_km={km}` | Поиск в радиусе |
| GET | `/organizations/search/rectangle?min_latitude={min_lat}&max_latitude={max_lat}&min_longitude={min_lng}&max_longitude={max_lng}` | Поиск в области |

### Справочники

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/buildings` | Все здания |
| GET | `/activities` | Все виды деятельности |

## Примеры запросов

### Получить все организации
```bash
curl -H 'X-API-Key: api-key' http://localhost:8000/organizations
```

### Поиск по названию
```bash
curl -H 'X-API-Key: api-key' "http://localhost:8000/organizations/search/name?name=Рога"
```

### Поиск по виду деятельности
```bash
curl -H 'X-API-Key: api-key' http://localhost:8000/organizations/activity/1
```

### Поиск в радиусе
```bash
curl -H 'X-API-Key: api-key' "http://localhost:8000/organizations/search/radius?latitude=55.7558&longitude=37.6176&radius_km=5"
```

### Поиск в прямоугольной области
```bash
curl -H 'X-API-Key: api-key' "http://localhost:8000/organizations/search/rectangle?min_latitude=55.7&max_latitude=55.8&min_longitude=37.6&max_longitude=37.7"
```

## Структура данных

### Организация
```json
{
  "id": 1,
  "name": "ООО Рога и Копыта",
  "phones": ["2-222-222", "3-333-333"],
  "building": {
    "id": 1,
    "address": "г. Москва, ул. Ленина 1, офис 3",
    "latitude": 55.7558,
    "longitude": 37.6176
  },
  "activities": [
    {
      "id": 2,
      "name": "Мясная продукция",
      "parent_id": 1
    }
  ]
}
```

### Здание
```json
{
  "id": 1,
  "address": "г. Москва, ул. Ленина 1, офис 3",
  "latitude": 55.7558,
  "longitude": 37.6176
}
```

### Вид деятельности
```json
{
  "id": 1,
  "name": "Еда",
  "parent_id": null,
  "children": [
    {
      "id": 2,
      "name": "Мясная продукция",
      "parent_id": 1
    }
  ]
}
```

## Особенности

- **Иерархический поиск**: Поиск по виду деятельности находит все подкатегории
- **Геопространственный поиск**: Поиск по радиусу и прямоугольной области
- **CORS поддержка**: Работает с веб-интерфейсом
- **API Key аутентификация**: Статический ключ для доступа

## Файлы проекта

- `simple_app.py` - Основное приложение (HTTP сервер)
- `advanced_test.html` - Веб-интерфейс для тестирования API
- `README.md` - Документация

## Технические детали

- **Язык**: Python 3
- **HTTP сервер**: Встроенный `http.server`
- **База данных**: In-memory (SQLite)
- **Аутентификация**: API Key в заголовке `X-API-Key`
- **Формат данных**: JSON
