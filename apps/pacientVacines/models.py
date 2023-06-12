from django.db import models
from employee.models import Employee
from vacinationLocal.models import VacinationLocal
from pacient.models import Pacient

class PacientVaccines(models.Model):
    applied_in = models.DateTimeField("Aplicada em", null=False)
    vaccine_dose = models.IntegerField("Dose da vacina", default=1)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE, default=0)
    vaccination_local = models.ForeignKey(VacinationLocal, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Vacinas do paciente"
        ordering = ["id"]

    def __str__(self):
        return f"{self.pacient} - {self.vaccine_dose} - {self.employee} - {self.vaccination_local} - {self.applied_in}"