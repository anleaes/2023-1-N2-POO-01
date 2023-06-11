from .models import localStorage
from rest_framework.models import serializers as Serializer

class LocalStorageSerializer(Serializer.ModelSerializer):
    class Meta:
        model = localStorage
        fields = '__all__'