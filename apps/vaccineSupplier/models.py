from django.db import models

class FornecedorVacina(models.Model):
    razao_social = models.CharField('razao_social', max_length=70)
    nome_fantasia = models.CharField('nome_fantasia', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=13)
    nome_dono = models.CharField('nome_dono', max_length=50)    

    class Meta:
        verbose_name = 'Fornecedor da vacina'
        ordering =['id']

    def __str__(self):
        return f"{self.nome_fantasia} - {self.cnpj}"