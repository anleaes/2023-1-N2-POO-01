from django.shortcuts import render
from rest_framework import serializers
from .models import vaccineScheduling

class vaccineschedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = vaccineScheduling
        fields = '__all__'