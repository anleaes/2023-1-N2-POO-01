from .models import Vacina
from rest_framework import serializers

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'