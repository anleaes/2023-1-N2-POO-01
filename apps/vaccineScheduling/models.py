from django.db import models

class AgendamentoVacina:
    def __init__(self, id, data, paciente, funcionario, vacina):
        self.id = id
        self.data = data
        self.paciente = paciente
        self.funcionario = funcionario
        self.vacina = vacina

def __str__(self):
        return self.agendamento
