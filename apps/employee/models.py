from django.db import models
from vacinationLocal.models import VacinationLocal

# Create your models here.
class Employee(models.Model):
    code = models.IntegerField("Código", default=0, null=False)
    full_name = models.CharField("Nome completo", max_length=120, null=False, default='Incompleto')
    age = models.IntegerField("Idade", default=0 ,null=False)
    function = models.CharField("Função", max_length=150, null=False, default='Não informado')
    formation = models.CharField("Formação", max_length=120, null=False, default='Não informado')
    vacination_local = models.ForeignKey(VacinationLocal, on_delete=models.CASCADE, related_name="local_funcionario", default=0)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['id']

    def __str__(self):
        return f"{self.code} - {self.full_name} - {self.age} - {self.function} - {self.vacination_local}"
