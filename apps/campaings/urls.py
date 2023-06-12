from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'campaings'

router = routers.DefaultRouter()
router.register('todas', views.campaignViewSet, basename='campaings')

urlpatterns = [
    path('', include(router.urls) )
]