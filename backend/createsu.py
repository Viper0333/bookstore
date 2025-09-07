import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()  # Carrega todas as apps do Django

from django.contrib.auth import get_user_model

# Função segura para uso direto no manage.py
def create_superuser_direct():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superusuário '{username}' criado.")
    else:
        print(f"ℹ️ Superusuário '{username}' já existe.")

# Função opcional para signals (como post_migrate)
def create_superuser(sender, **kwargs):
    create_superuser_direct()
