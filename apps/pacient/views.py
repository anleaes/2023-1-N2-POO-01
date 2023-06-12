from django.shortcuts import render
from .models import Pacient	
from rest_framework import viewsets
from .serializers import pacientSerializer


class PacientViewSet(viewsets.ModelViewSet):
    queryset = Pacient.objects.all()
    serializer_class = pacientSerializer