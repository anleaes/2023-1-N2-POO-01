from rest_framework import serializers
from .models import pacientVacines

class PacienteSerializer(serializers.ModelSerializer):
    local = vacinationLocalSerializer()

    class Meta:
        model = pacientVacines
        fields = ('id', 'dose', 'funcionario', 'aplicada_em', 'paciente')
