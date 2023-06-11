from django.db import models

class pacientVacines(models.Model):
    codigo = models.IntegerField()
    paciente = models.CharField('paciente', max_length=100)
    funcionario = models.IntegerField()
    dose = models.CharField(max_length=100)
    aplicada_em = models.CharField(max_length=100)

def __str__(self):
        return self.paciente
