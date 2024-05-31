################################
# PYTHON-BASE
################################
FROM python:3.12-slim as python-base

# Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # pip
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.8.3 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    # never create virtual environment automaticly, only use env prepared by us
    POETRY_VIRTUALENVS_CREATE=false \
    \
    # this is where our requirements + virtual environment will live
    VIRTUAL_ENV="/venv"

# prepend poetry and venv to path
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

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
# The --mount will mount the buildx cache directory to where
# Poetry and Pip store their cache so that they can re-use it
RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python3 -

# used to init dependencies
WORKDIR /app
COPY poetry.lock pyproject.toml ./


# install runtime deps to $VIRTUAL_ENV
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root --only main


################################
# DEVELOPMENT
################################
FROM builder-base as development

WORKDIR /app

# quicker install as runtime deps are already installed
RUN --mount=type=cache,target=/root/.cache \
    poetry install --no-root 

COPY . ./

# build static files
RUN poetry run python manage.py collectstatic --no-input

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]


################################
# PRODUCTION
################################
FROM python-base as production

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

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $VIRTUAL_ENV $VIRTUAL_ENV
COPY --from=builder-base $CPLUS_INCLUDE_PATH $CPLUS_INCLUDE_PATH
COPY --from=builder-base $C_INCLUDE_PATH $C_INCLUDE_PATH


WORKDIR /app
COPY . ./
COPY poetry.lock pyproject.toml ./

# build static files
RUN poetry run python manage.py collectstatic --no-input
# Install Gunicorn
RUN poetry add gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "config.wsgi:application"]