from django.shortcuts import render
from .models import vaccineScheduling
from rest_framework import viewsets
from .serializer import vaccineschedulingSerializer

class vaccineschedulingViewSet(viewsets.ModelViewSet):
    queryset = vaccineScheduling.objects.all()
    serializer_class = vaccineschedulingSerializer