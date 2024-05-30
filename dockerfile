# Укажите базовый образ
FROM python:3.12-slim

# Установите зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Установите Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавьте Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы проекта
COPY . /app

# Копируйте .env файл
COPY config/.env /app/config/.env

# Установите зависимости через Poetry
RUN poetry install --no-root

# Настройте команду запуска
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
