# Etapa base: define ambiente
FROM python:3.11-slim as python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/opt/poetry/bin:$PATH"

# Instala dependências básicas e Poetry
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl build-essential libpq-dev gcc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version \
    && apt-get purge --auto-remove -y build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Etapa build: instala dependências com Poetry
FROM python-base as builder

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --only main

# Etapa final (produção/dev)
FROM python-base

WORKDIR /app

# Copia o ambiente virtual do builder
COPY --from=builder /app/.venv /app/.venv

# Copia o restante da aplicação
COPY . .

# Ativa o virtualenv no PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expondo porta padrão do Django
EXPOSE 8000

# Variável de controle de ambiente
ENV DJANGO_ENV=prod

# Entrada: muda comando conforme ambiente
CMD if [ "$DJANGO_ENV" = "dev" ]; then \
        poetry run python manage.py runserver 0.0.0.0:8000; \
    else \
        poetry run python manage.py collectstatic --noinput && \
        poetry run gunicorn bookstore.wsgi:application --bind 0.0.0.0:8000 --workers 4; \
    fi


