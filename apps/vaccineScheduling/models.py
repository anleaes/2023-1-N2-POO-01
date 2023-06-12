from django.db import models
from employee.models import Employee
from vacinationLocal.models import VacinationLocal
from vaccines.models import Vacina
from pacient.models import Pacient

class vaccineScheduling(models.Model):
    scheduling_date = models.DateTimeField("Data agendada", null=False)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, related_name="pacient", default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee")
    vaccine = models.ForeignKey(Vacina, on_delete=models.CASCADE, related_name="vaccine")
    vacination_local = models.ForeignKey(VacinationLocal, on_delete=models.CASCADE, related_name="vacination_local")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)


    class Meta:
        verbose_name = "Agenda de Vacina"
        verbose_name_plural = "Agenda de Vacinas"
        ordering = ['id']

    
    def __str__(self):
        return f"{self.scheduling_date} - {self.pacient} - {self.employee} - {self.vaccine} - {self.vacination_local} - {self.created_at}"