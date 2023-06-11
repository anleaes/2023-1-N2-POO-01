from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    local = vacinationLocalSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'codigo', 'nome_completo', 'idade', 'funcao', 'formacao', 'local')