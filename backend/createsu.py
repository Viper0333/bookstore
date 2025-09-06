from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
import os

def create_superuser(sender, **kwargs):
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuário '{username}' criado com sucesso!")

def setup_superuser():
    if os.environ.get("CREATE_SUPERUSER") == "1":
        post_migrate.connect(create_superuser)
