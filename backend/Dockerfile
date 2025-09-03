# Base image
FROM python:3.13-slim

# ----------------------
# Environment variables
# ----------------------
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

# Prepend Poetry and virtualenv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# ----------------------
# Install system dependencies
# ----------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ----------------------
# Install Poetry
# ----------------------
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && $POETRY_HOME/bin/poetry --version

# ----------------------
# Set working directory for Poetry install
# ----------------------
WORKDIR $PYSETUP_PATH

# Copy dependency files first (leverage Docker cache)
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN $POETRY_HOME/bin/poetry install --no-dev

# ----------------------
# Copy application code
# ----------------------
WORKDIR /app
COPY . /app/

# Expose port
EXPOSE 8000

# ----------------------
# Run the Django server
# ----------------------
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
