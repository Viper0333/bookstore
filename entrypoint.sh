#!/bin/sh

# Aplicar migrações automaticamente
python manage.py migrate --noinput

# Coletar arquivos estáticos (se tiver)
python manage.py collectstatic --no-input

# Iniciar Gunicorn
exec gunicorn bookstore.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --access-logfile /dev/null \
    --log-level warning
