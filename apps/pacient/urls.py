from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pacient'

router = routers.DefaultRouter()
router.register('todos', views.PacientViewSet, basename='Pacientes')

urlpatterns = [
    path('', include(router.urls) )
]