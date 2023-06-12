from typing import Self
from django.db import models
from vaccines.models import Vacina

class Campaings (models.Model):
    campaing_name = models.CharField ("Nome da campanha", max_length=60, null=False)
    start_in = models.DateTimeField ("Data de início", null=False)
    end_in = models.DateTimeField ("Data de término", null=False)
    vaccine_type = models.ForeignKey(Vacina, on_delete=models.CASCADE)

    class Meta:
            verbose_name = 'Campanha'
            verbose_name_plural = 'Campanhas'
            ordering =['id']

    def __str__(self):
        return f"{self.campaing_name} - {self.start_in} - {self.end_in} - {self.vaccine_type}"