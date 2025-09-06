from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from .createsu import setup_superuser
        setup_superuser()

class TwitterCloneConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "twitter_clone"

    def ready(self):
        from .createsu import setup_superuser
        setup_superuser()


