from django.apps import AppConfig


class MyusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myusers'
    
    def ready(self) -> None:
        import myusers.signals
