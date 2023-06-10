from django.shortcuts import render
from rest_framework import viewsets
from .models import VacinationLocal
from .serializers import vacinationLocalSerializer

class vacinationLocalViewSet(viewsets.ModelViewSet):
    queryset = vacinationLocal.objects.all()
    serializer_class = vacinationLocalSerializer