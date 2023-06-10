from rest_framework import serializers
from .models import VacinationLocal

class VacinationLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacinationLocal
        fields = ('nome', 'endereco')