from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'campaigns'

router = routers.DefaultRouter()
router.register('todas', views.campaignViewSet, basename='Campanhas')

urlpatterns = [
    path('', include(router.urls))
]