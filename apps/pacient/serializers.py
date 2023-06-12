from .models import Pacient
from rest_framework import serializers as Serializer

class pacientSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Pacient
        fields = '__all__'