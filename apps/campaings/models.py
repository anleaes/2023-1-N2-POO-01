from typing import Any, Self
from django.db import models

# Create your models here.
class Campaings (models.Model):
    def __init__(self, id, nome_campanha, comeca_em, termina_em, tipo):
        self._id = None
        self._nome_campanha = models.CharField(max_length=100)
        self._comeca_em = models.DateField ()
        self._termina_em = models.DateField ()
        self._tipo = models.CharField(max_length=200)

        