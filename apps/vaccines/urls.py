from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vaccines'

router = routers.DefaultRouter()
router.register('todas', views.VacinaViewSet, basename='Vacinas')

urlpatterns = [
    path('', include(router.urls) )
]
