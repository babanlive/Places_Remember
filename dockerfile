################################
# PYTHON-BASE
################################
FROM python:3.12-slim as python-base

# Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ENV POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUAL_ENV="/venv"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

# prepare virtual env
RUN python -m venv $VIRTUAL_ENV

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
    python3-pip \
    libgdal-dev \
    locales \
    curl \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root --only main


################################
# DEVELOPMENT
################################
FROM builder-base as dev

WORKDIR /app

# quicker install as runtime deps are already installed
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root 

COPY . ./

RUN poetry run python manage.py collectstatic --no-input

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

################################
# PRODUCTION
################################
FROM python-base as prod

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-pip \
    libgdal-dev \
    locales \
    curl \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $VIRTUAL_ENV $VIRTUAL_ENV
COPY --from=builder-base $CPLUS_INCLUDE_PATH $CPLUS_INCLUDE_PATH
COPY --from=builder-base $C_INCLUDE_PATH $C_INCLUDE_PATH

WORKDIR /app
COPY . ./
COPY poetry.lock pyproject.toml ./

RUN poetry run python manage.py collectstatic --no-input
RUN poetry add gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "config.wsgi:application"]