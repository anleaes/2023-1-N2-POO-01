from django.db import models

class FornecedorVacina(models.Model):
    id = models.CharField('id', max_length=10)
    razao_social = models.CharField('razao_social', max_length=70)
    nome_fantasia = models.CharField('nome_fantasia', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=13)
    nome_dono = models.CharField('nome_dono', max_length=30)    

    class Meta:
        verbose_name = 'FornecedorVacina'
        verbose_name_plural = 'FornecedoresVacina'
        ordering =['id']

    def __str__(self):
        return self.name        
