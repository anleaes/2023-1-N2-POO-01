from django.shortcuts import render
from rest_framework import viewsets
from .models import LocalVacina
from .serializers import LocalVacinaSerializer

class LocalVacinaViewSet(viewsets.ModelViewSet):
    queryset = LocalVacina.objects.all()
    serializer_class = LocalVacinaSerializer