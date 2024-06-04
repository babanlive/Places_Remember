################################
# PYTHON-BASE
################################
FROM python:3.12-slim as python-base

# Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

ENV POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUAL_ENV="/venv"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

# working directory and Python path
WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

################################
# BUILDER-BASE
################################
FROM python-base as builder-base
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libgdal-dev \
    locales \
    curl \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/ * 

RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root  --only main 
    
COPY . ./

################################
#PRODACTION
################################
FROM builder-base as prod
RUN poetry add gunicorn
RUN poetry run python manage.py collectstatic --noinput --clear

################################
#DEVELOPMENT
################################
FROM builder-base as dev
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root
