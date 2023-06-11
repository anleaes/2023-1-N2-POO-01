from django.shortcuts import render
from rest_framework import viewsets
from .models import VacinationLocal
from .serializers import vacinationLocalSerializer

class VacinationLocalViewSet(viewsets.ModelViewSet):
    queryset = VacinationLocal.objects.all()
    serializer_class = vacinationLocalSerializer