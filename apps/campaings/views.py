from django.shortcuts import render
from .models import Campaings as Campanha
from rest_framework import viewsets
from .serializers import CampaingsSerializer


class campaignViewSet(viewsets.ModelViewSet):
    queryset = Campanha.objects.all()
    serializer_class = CampaingsSerializer