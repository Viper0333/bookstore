from django.apps import AppConfig
import createsu

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    # def ready(self):
    #     createsu.setup_superuser_creation()



