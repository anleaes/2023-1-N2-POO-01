from django.db import models

class pacientVacines:
    def __init__(self, id, aplicada_em, dose, funcionario, paciente):
        self.id = id
        self.aplicada_em = aplicada_em
        self.dose = dose
        self.funcionario = funcionario
        self.paciente = paciente

def __str__(self):
        return self.paciente
