from django.shortcuts import render
from .models import localStorage
from rest_framework import viewsets
from .serializer import localStorageSerializer


class localStorageViewSet(viewsets.ModelViewSet):
    queryset = localStorage.objects.all()
    serializer_class = localStorageSerializer