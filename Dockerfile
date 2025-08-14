# Etapa base para configuração do Python e Poetry
FROM python:3.11-slim as python-base

# Configuração de variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Ajusta PATH para incluir Poetry e venv
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências de sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Instala Poetry atualizado
RUN pip install --no-cache-dir poetry==1.8.3

# Instala psycopg2 (opcional — poderia ir no pyproject.toml)
RUN pip install --no-cache-dir psycopg2

# Define pasta de instalação das deps
WORKDIR $PYSETUP_PATH

# Copia apenas arquivos de dependências para otimizar cache
COPY poetry.lock pyproject.toml ./

# Instala dependências (sem dev, se for produção)
RUN poetry install --no-root --without dev

# Define pasta final da aplicação
WORKDIR /app

# Copia código para a imagem
COPY . /app/

# Expõe porta
EXPOSE 8000

# Comando default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
