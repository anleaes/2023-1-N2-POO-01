from django.urls import path, include
from .views import pacientViewSet
from rest_framework import routers

app_name = 'pacientVacines'

router = routers.DefaultRouter()
router.register('pacientVacines', views.PacientViewSet)

urlpatterns = [

    path('', include(router.urls)), 
]
