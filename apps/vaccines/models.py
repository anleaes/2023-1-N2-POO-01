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

