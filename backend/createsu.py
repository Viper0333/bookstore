import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

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

# conecta ao signal post_migrate
def setup_superuser_creation():
    post_migrate.connect(lambda sender, **kwargs: create_superuser_direct())
