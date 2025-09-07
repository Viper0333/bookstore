from django.apps import AppConfig
import createsu

class TweetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tweets"

    def ready(self):
        createsu.setup_superuser_creation()

