from django.shortcuts import render
from .models import pacient
from rest_framework import viewsets
from .serializer import PacientSerializer

class PacientViewSet(viewsets.ModelViewSet):
    queryset = pacient.objects.all()
    serializer_class = pacientSerializer 
