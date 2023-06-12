from rest_framework import serializers
from .models import PacientVaccines

class pacientVacinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacientVaccines
        fields = '__all__'
