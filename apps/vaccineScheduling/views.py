from django.shortcuts import render
from .models import vaccinescheduling
from rest_framework import viewsets
from .serializer import vaccineschedulingSerializer

class vaccineschedulingViewSet(viewsets.ModelViewSet):
    queryset = vaccinescheduling.objects.all()
    serializer_class = vaccineschedulingSerializer