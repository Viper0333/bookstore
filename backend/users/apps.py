from django.apps import AppConfig

class TweetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"  # Corrigi o nome aqui também (estava "twaeets")

    def ready(self):
        from createsu import setup_superuser_creation  # ✅ Importa aqui dentro
        setup_superuser_creation()
