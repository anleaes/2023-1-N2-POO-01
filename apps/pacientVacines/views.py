from django.shortcuts import render
from .models import PacientVaccines
from rest_framework import viewsets
from .serializer import pacientVacinesSerializer

class PacientViewSet(viewsets.ModelViewSet):
    queryset = PacientVaccines.objects.all()
    serializer_class = pacientVacinesSerializer
