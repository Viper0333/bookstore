#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twitter_clone.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Cria superusuário automático se variáveis de ambiente existirem
    if os.environ.get("CREATE_SUPERUSER") == "1":
        from createsu import create_superuser
        create_superuser()

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
