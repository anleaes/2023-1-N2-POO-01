from .models import FornecedorVacina
from rest_framework import serializers

class FornecedorVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorVacina
        fields = '__all__'