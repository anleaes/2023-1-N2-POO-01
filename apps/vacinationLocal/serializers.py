from rest_framework import serializers
from .models import VacinationLocal

class vacinationLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacinationLocal
        fields = '__all__'