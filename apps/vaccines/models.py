from django.db import models
from vaccineSupplier.models import FornecedorVacina
from datetime import date

class Vacina(models.Model):
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
        
    def adicionar_vacina(vacinas, nome_vacina, tipo_vacina,doses_necessarias, forma_armazenamento, temperatura, intervalo_entre_doses, numero_lote, fabricada_em, validade, fornecedor):
        nova_vacina = Vacina(nome_vacina, tipo_vacina, doses_necessarias, forma_armazenamento, temperatura, intervalo_entre_doses, numero_lote, fabricada_em, validade, fornecedor)
        vacinas.append(nova_vacina)
        print("Vacina adicionada com sucesso!")

    @staticmethod
    def listar_vacinas(vacinas):
          for vacina in vacinas:
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
            print(f"Nome: {vacina._nome_vacina}")
            print(f"Validade: {vacina._validade}")
            print()     
   
class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering =['id']

def __str__(self):
        return f"{self.nome_vacina} - {self.tipo_vacina} - {self.doses_necessarias} - {self.forma_armazenamento} - {self.temperatura} - {self.validade} - {self.intervalo_entre_doses} - {self.numero_lote} - {self.fabricada_em} - {self.fornecedor}"