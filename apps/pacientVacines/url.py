from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pacientVacines'

router = routers.DefaultRouter()
router.register('todas', views.PacientViewSet, basename='Vacinas dos pacientes')

urlpatterns = [

    path('', include(router.urls)), 
]
