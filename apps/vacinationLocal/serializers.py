from rest_framework import serializers
from .models import LocalVacina

class LocalVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalVacina
        fields = ('nome', 'endereco')