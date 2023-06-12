from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pacient'

router = routers.DefaultRouter()
router.register('listar', views.PacientViewSet, basename='pacient')

urlpatterns = [
    path('', include(router.urls) )
]