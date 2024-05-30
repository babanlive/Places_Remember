# Проект Places Remember

Данный проект написан по ТЗ "Очень Интересно"

## Описание проекта

Проект представляет из веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещенных местах.

## Технологии и инструменты

- Python 3.12
- Django 5.0.6
- Postgis
- Docker (поднимает контейнеры Postgis)
- Bootstrap 5 / HTML / CSS


## Установка и запуск проекта

1. Установка gdal (требуется для работы с различными геопространственными данными ):
ля Linux, выполните следующую команду в терминале:

```shell
sudo apt install build-essential libsqlite3-dev libspatialite-dev
```
```shell
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt update
sudo apt install gdal-bin
```

2. Установка Poetry
Для Linux, выполните следующую команду в терминале:
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Для Windows, выполните следующую команду в PowerShell:
```power shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Other os
[Instruction](https://python-poetry.org/docs/#installation)

3. Клонируйте репозиторий и перейдите в папку проекта:

```shell
git clone git@github.com:babanlive/Places_Remember.git && cd Places_Remember
```

4. Установка проекта:

```shell
poetry install
```

5. С помощью Docker Compose запустите контейнеры Postgis:

`docker compose up -d`

6. Примените миграции:

`python manage.py migrate`

7. Создайте суперпользователя (для доступа к административной панели):

`python manage.py createsuperuser`

8. Запустите сервер разработки:

```shell
poetry run python manage.py runserver
```

9. Откройте браузер и перейдите по адресу `http://localhost:8000/`.

## Не реализованые функци (TODO)

1. По ТЗ требуется вход через vk или mail.ru, но при использовании http://localhost:8000/ удалось реализовать вход толлько через GitHub

2. Через bootstrap не оформлен код шаблонов входа пользователя систему. (остаются по умолчанию от django-allauth)