from django.apps import AppConfig


class AppServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_service'

    def ready(self):
        import app_service.signals
