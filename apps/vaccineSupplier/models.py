from django.db import models

class FornecedorVacina(models.Model):
    razao_social = models.CharField('razao_social', max_length=70)
    nome_fantasia = models.CharField('nome_fantasia', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=13)
    nome_dono = models.CharField('nome_dono', max_length=30)    

    @staticmethod
    def adicionar_fornecedor(fornecedores, razao_social, nome_fantasia, cnpj, nome_dono):
        novo_fornecedor = FornecedorVacina(razao_social, nome_fantasia, cnpj, nome_dono)
        fornecedores.append(novo_fornecedor)
        print("Fornecedor adicionado com sucesso!")

    @staticmethod
    def listar_fornecedores(fornecedores):
        for fornecedor in fornecedores:
            print(f"Razão Social: {fornecedor._razao_social}")
            print(f"Nome Fantasia: {fornecedor._nome_fantasia}")
            print(f"CNPJ: {fornecedor._cnpj}")
            print(f"Nome do Dono: {fornecedor._nome_dono}")
            print()
            
    @staticmethod
    def buscar_fornecedor_por_cnpj(fornecedores, cnpj):
        for fornecedor in fornecedores:
            if fornecedor._cnpj == cnpj:
                print(f"Razão Social: {fornecedor._razao_social}")
                print(f"Nome Fantasia: {fornecedor._nome_fantasia}")
                print(f"CNPJ: {fornecedor._cnpj}")
                print(f"Nome do Dono: {fornecedor._nome_dono}")
                return
        print("Fornecedor não encontrado.")

    class Meta:
        verbose_name = 'FornecedorVacina'
        verbose_name_plural = 'FornecedoresVacina'
        ordering =['id']

    def __str__(self):
        return self.name        
