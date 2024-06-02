# Проект Places Remember

Данный проект написан по ТЗ ООО "Очень Интересно" г. Красноярск

## Описание проекта

Проект представляет из себя веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещенных местах.

## Технологии и инструменты

- Python 3.12
- Django 5.0.6
- GDal
- Leaflet
- Postgis
- Docker (Запуск проекта и базы данных в контерйнере)
- Bootstrap 5 / HTML / CSS


## Установка и запуск проекта

1. Клонируйте репозиторий и перейдите в папку проекта:
```shell
git clone git@github.com:babanlive/Places_Remember.git && cd Places_Remember
```

2. Создание файла .env
- Создайте в папке `config` файл `.env` согласно образцу [env_example](config/.env.example)

3. Запуск проекта через Docker
- Для запуска в режиме разработки выполните команду:
```shell
docker-compose -f docker-compose.dev.yaml up --build
```

- Для запуска в режиме производства выполните команду:
```shell
docker-compose -f docker-compose.prod.yaml up --build
```

4. Выполните миграции 
```shell
docker exec -it app_django poetry run python manage.py migrate
```

5. Откройте браузер и перейдите по адресу http://localhost:8000/.

## Cоздать суперпользователя

```shell
docker exec -it app_django poetry run python manage.py createsuperuser
```

## Запустить тесты
```shell
docker exec -it app_django poetry run python manage.py test
```

## Нереализованые функции (TODO)

1. По ТЗ требуется вход через vk или mail.ru, но при использовании http://localhost:8000/ удалось реализовать вход только через GitHub

2. Через bootstrap не оформлен код шаблонов входа пользователя систему. (остаются по умолчанию от django-allauth)

3. Не рализованы функции использования `github actions`
