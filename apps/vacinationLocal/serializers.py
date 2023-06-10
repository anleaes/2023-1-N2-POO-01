from rest_framework import serializers
from .models import vacinationLocal

class vacinationLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = vacinationLocal
        fields = ('nome', 'endereco')