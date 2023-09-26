# Админка менеджеров FoodPlan

## Установка и запуск
Установка через [Poetry](https://python-poetry.org). Склонируйте репозиторий и запустите установку. Poetry сама создать окружение:

```sh
poetry install
```

Далее, накатите миграции:

```sh
poetry run python manage.py migrate
```

и запустите сервер:

```sh
poetry run python manage.py runserver
```
