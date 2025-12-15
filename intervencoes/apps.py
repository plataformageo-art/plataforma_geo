from django.apps import AppConfig


class IntervencoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'intervencoes'

def ready(self):
        import intervencoes.signals  # importa o arquivo signals para registrar o listener