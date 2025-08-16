#!/bin/sh
set -e

echo ">> Rodando entrypoint.sh..."

# Aplica migrations
python manage.py migrate --noinput

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Executa o comando passado (ex: gunicorn ou runserver)
exec "$@"
