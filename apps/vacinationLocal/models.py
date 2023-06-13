from django.db import models

class VacinationLocal(models.Model):
    local_name = models.CharField("Nome do local", max_length=100)
    street = models.CharField("Rua", max_length=100)
    neighborhood = models.CharField("Bairro", max_length=100, default=None)
    cep = models.IntegerField("CEP", default=0)
    number = models.IntegerField("Número", default=0)
    complement = models.CharField("Complemento", max_length=100)
    reference = models.CharField("Referência", max_length=100)

    class Meta:
        verbose_name = "Local de vacinação"
        verbose_name_plural = "Locais de vacinação"
        ordering = ["id"]

    def __str__(self):
        return f"{self.local_name} - {self.street} - {self.cep} - {self.number}"
    
