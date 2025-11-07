# Incident API Service

API-сервис для учета событий в системах городской мобильности.

## Запуск приложения

1. Установите зависимости:

   pip install -r requirements.txt

2. Запустите сервер:

    uvicorn app.main:app --reload

3. Откройте документацию API: 

   http://127.0.0.1:8000/docs

## Эндпоинты

**Создать событие**

    POST /incidents/

Тело запроса:

    json
    {
      "description": "Самокат не в сети",
      "status": "open",
      "source": "operator"
    }

**Получить список событий**

    GET /incidents/

**Параметры:**

    status - фильтр по статусу
    skip - пропуск записей (по умолчанию 0)
    limit - лимит записей (по умолчанию 100)

**Получить событие по ID**

    GET /incidents/{incident_id}

**Обновить статус события**

    PATCH /incidents/{incident_id}

Тело запроса:

    json
    {
      "status": "in_progress"
    }

**Статусы событий**

    open - открыт
    in_progress - в работе
    resolved - решен
    closed - закрыт

**Источники событий**

    operator - оператор
    monitoring - мониторинг
    partner - партнер

**Тестирование API**

После запуска сервера откройте http://127.0.0.1:8000/docs для интерактивного тестирования API через Swagger UI.

**Примеры команд curl:
Создать событие:**

  bash
  curl -X POST "http://127.0.0.1:8000/incidents/" \
       -H "Content-Type: application/json" \
       -d '{"description": "Точка не отвечает", "source": "monitoring"}'

**Получить все события:**

    bash
    curl "http://127.0.0.1:8000/incidents/"
    
**Обновить статус:**

    bash
    curl -X PATCH "http://127.0.0.1:8000/incidents/1" \
         -H "Content-Type: application/json" \
         -d '{"status": "resolved"}'

**Структура проекта**

incident_api/
├── app/
│   ├── main.py          # Основное приложение FastAPI
│   ├── models.py        # Модели базы данных
│   ├── schemas.py       # Pydantic схемы
│   └── database.py      # Настройки базы данных
├── requirements.txt     # Зависимости
└── incidents.db        # Файл базы данных (создается автоматически)
