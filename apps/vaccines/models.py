from django.db import models
from vaccines.models import Vacina
from datetime import date

class Vacina:
    
     def __init__(self, id, nome_vacina, tipo_vacina, doses_necessarias, forma_armazenamento, temperatura, intervalo_entre_doses, numero_lote, fabricada_em, validade, fornecedor):
        self._id = id          
        self._nome_vacina = nome_vacina
        self._tipo_vacina = tipo_vacina
        self._doses_necessarias = doses_necessarias
        self._forma_armazenamento = forma_armazenamento
        self._temperatura = temperatura
        self._intervalo_entre_doses = intervalo_entre_doses
        self._numero_lote = numero_lote
        self._fabricada_em = fabricada_em
        self._validade = validade
        self._fornecedor = fornecedor  
        
     def adicionar_vacina(vacinas, id, nome_vacina, tipo_vacina,doses_necessarias, forma_armazenamento, temperatura, intervalo_entre_doses, numero_lote, fabricada_em, validade, fornecedor):
        nova_vacina = Vacina(id, nome_vacina, tipo_vacina, doses_necessarias, forma_armazenamento, temperatura, intervalo_entre_doses, numero_lote, fabricada_em, validade, fornecedor)
        vacinas.append(nova_vacina)
        print("Vacina adicionada com sucesso!")

     @staticmethod
     def listar_vacinas(vacinas):
          for vacina in vacinas:
            print(f"ID: {vacina._id}")
            print(f"Nome: {vacina._nome_vacina}")
            print(f"Tipo: {vacina._tipo_vacina}")
            print(f"Doses Necessárias: {vacina._doses_necessarias}")
            print(f"Forma de Armazenamento: {vacina._forma_armazenamento}")
            print(f"Temperatura: {vacina._temperatura}")
            print(f"Intervalo entre Doses: {vacina._intervalo_entre_doses}")
            print(f"Número do Lote: {vacina._numero_lote}")
            print(f"Fabricada em: {vacina._fabricada_em}")
            print(f"Validade: {vacina._validade}")
            print(f"Fornecedor: {vacina._fornecedor}")
            print()
            
     def checar_validade(vacinas):
        data_atual = date.today()
        vacinas_vencidas = []

        for vacina in vacinas:
          data_validade = date.fromisoformat(vacina._validade)
          if data_validade < data_atual:
              vacinas_vencidas.append(vacina)

        if len(vacinas_vencidas) == 0:
          print("Não há vacinas vencidas.")
        else:
          print("Vacinas vencidas:")
          for vacina in vacinas_vencidas:
            print(f"ID: {vacina._id}")
            print(f"Nome: {vacina._nome_vacina}")
            print(f"Validade: {vacina._validade}")
            print()

class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering =['id']

def __str__(self):
        return self.name