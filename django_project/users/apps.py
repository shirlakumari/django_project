from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# in documentation given that import signals.py file
    def ready(self):
        from . import signals