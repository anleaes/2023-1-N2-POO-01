from django.db import models
from vaccineSupplier.models import FornecedorVacina

class FornecedorVacina:
     def __init__(self, id, razao_social, nome_fantasia, cnpj, nome_dono):
       self._id = id
       self._razao_social = razao_social
       self._nome_fantasia = nome_fantasia
       self._cnpj = cnpj
       self._nome_dono = nome_dono       

     @staticmethod
     def adicionar_fornecedor(fornecedores, id, razao_social, nome_fantasia, cnpj, nome_dono):
        novo_fornecedor = FornecedorVacina(id, razao_social, nome_fantasia, cnpj, nome_dono)
        fornecedores.append(novo_fornecedor)
        print("Fornecedor adicionado com sucesso!")

     @staticmethod
     def listar_fornecedores(fornecedores):
        for fornecedor in fornecedores:
            print(f"ID: {fornecedor._id}")
            print(f"Razão Social: {fornecedor._razao_social}")
            print(f"Nome Fantasia: {fornecedor._nome_fantasia}")
            print(f"CNPJ: {fornecedor._cnpj}")
            print(f"Nome do Dono: {fornecedor._nome_dono}")
            print()
            
    