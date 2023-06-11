from django.db import models
from vaccineSupplier.models import FornecedorVacina
from datetime import date

class Vacina(models.Model):
    id = models.CharField('id', max_length=20)
    nome_vacina = models.CharField('nome_vacina', max_length=50)
    tipo_vacina = models.CharField('tipo_vacina', max_length=30)
    doses_necessarias = models.CharField('doses_necessarias', max_length=10)
    forma_armazenamento = models.CharField('forma_armazenamento', max_length=30)  
    temperatura = models.CharField('temperatura', max_length=50) 
    intervalo_entre_doses = models.CharField('intervalo_entre_doses', max_length=50)    
    numero_lote = models.CharField('numero_lote', max_length=50)     
    fabricada_em = models.DateField ('fabricada_em', max_length=10)
    validade = models.DateField ('validade', max_length=10)   
    fornecedor = models.ForeignKey(FornecedorVacina, on_delete=models.CASCADE)     
  
class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering =['id']

def __str__(self):
        return self.name