from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vaccinesScheduling'

router = routers.DefaultRouter()
router.register('todos', views.vaccineschedulingViewSet, basename='Agendamentos')

urlpatterns = [

    path('', include(router.urls)), 
]