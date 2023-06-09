from django.db import models
from vaccines.models import Vacina
from vacinationLocal.models import VacinationLocal

class localStorage(models.Model) :
    vaccine = models.ForeignKey(Vacina, related_name="vacina", on_delete=models.CASCADE)
    vacination_local = models.ForeignKey(VacinationLocal, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantidade",  default=0)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)


    class Meta: 
        verbose_name = "Estoque local"
        ordering = ["id"]


    def __str__(self):
        return f"{self.vaccine} - {self.quantity} - {self.created_at}"