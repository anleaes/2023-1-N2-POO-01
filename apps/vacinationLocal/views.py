from django.shortcuts import render
from rest_framework import viewsets
from .models import LocalVacina
from .serializers import VacinationLocalSerializer

class VacinationLocalViewSet(viewsets.ModelViewSet):
    queryset = VacinationLocal.objects.all()
    serializer_class = VacinationLocalSerializer