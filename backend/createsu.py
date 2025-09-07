import os
from django.db.models.signals import post_migrate

def create_superuser_direct():
    # ⛔ get_user_model não pode estar no topo do arquivo!
    from django.contrib.auth import get_user_model  # ✅ importado aqui dentro

    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superusuário '{username}' criado.")
    else:
        print(f"ℹ️ Superusuário '{username}' já existe.")

def setup_superuser_creation():
    if os.getenv("CREATE_SUPERUSER") == "1":
        post_migrate.connect(lambda sender, **kwargs: create_superuser_direct(), dispatch_uid="create_superuser_once")
