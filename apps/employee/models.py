from django.db import models

# Create your models here.
class Employee(models.Model):
    codigo = models.IntegerField()
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    funcao = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    local = models.ForeignKey(vacinationLocal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo