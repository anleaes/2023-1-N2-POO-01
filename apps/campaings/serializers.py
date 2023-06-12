from .models import Campaings
from rest_framework import serializers as Serializer

class CampaingsSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Campaings
        fields = '__all__'