from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #Ready ejecuta codigo cuando la aplicación se inicia, pero solo una vez durante el ciclo de vida de la aplicacion
    
    def ready(self):
        import users.signals