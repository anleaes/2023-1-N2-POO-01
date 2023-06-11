from .models import localStorage
from rest_framework import serializers as Serializer

class localStorageSerializer(Serializer.ModelSerializer):
    class Meta:
        model = localStorage
        fields = '__all__'