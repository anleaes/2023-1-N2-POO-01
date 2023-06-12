from django.apps import AppConfig


class PacientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pacient'
    verbose_name = 'Paciente'
    verbose_name_plural = 'Pacientes'