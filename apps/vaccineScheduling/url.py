from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vaccinesScheduling'

router = routers.DefaultRouter()
router.register('listar', views.vaccineschedulingViewSet, basename='vaccinescheduling')

urlpatterns = [

    path('', include(router.urls)), 
]