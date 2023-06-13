from django.db import models

class Pacient(models.Model):
    document = models.CharField("CPF", max_length=12, null=False, default=0)
    pacient_name = models.CharField("Nome do paciente", max_length=50, default="Não informado")
    age = models.IntegerField("Idade", null=False, default=0)
    GENDER_CHOICES = ('M', 'Masculino'),('F', 'Feminino'), ('O', 'Outro'), ('N_D', 'Não definido')
    gender = models.CharField("Gênero", max_length=3, choices=GENDER_CHOICES, null=False, default='N_D')
    phone = models.CharField("Telefone", max_length=12, null=False, default=0)
    street = models.CharField("Street", max_length=50, null=False, default="Não informado")
    neighborhood = models.CharField("Bairro", max_length=60, null=False, default="Não informado")
    postal_code = models.CharField("CEP", max_length=9, null=False)
    number = models.IntegerField("Número", null=False, default=0)
    complement = models.CharField("Complemento", max_length=100, null=True, default='Não informado')
    reference = models.CharField("Referência", max_length=100, null=True, default='Não informado')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering =['id']

    def __str__(self):
        return f"{self.document} - {self.pacient_name} - {self.age} - {self.gender} - {self.phone}"