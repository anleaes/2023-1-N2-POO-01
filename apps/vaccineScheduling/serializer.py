from django.shortcuts import render
from rest_framework import serializers
from .models import vaccinescheduling

class vaccineschedulingSerializer(serializers.ModelSerializer):
    local = vacinationLocalSerializer()

    class Meta:
        model = vaccinescheduling
        fields = ('id', 'data', 'funcionario', 'vacina', 'paciente')