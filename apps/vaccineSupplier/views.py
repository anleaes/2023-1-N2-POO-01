from django.shortcuts import render

from .models import FornecedorVacina

from rest_framework import viewsets
from .serializer import FornecedorVacinaSerializer

class FornecedorVacinaViewSet(viewsets.ModelViewSet):
    queryset = FornecedorVacina.objects.all()
    serializer_class = FornecedorVacinaSerializer  
