from django.apps import AppConfig


class GestionInmueblesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion_inmuebles'

    def ready(self):
        import gestion_inmuebles.signals  # Importa las señales