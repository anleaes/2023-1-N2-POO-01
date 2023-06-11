from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'campaings'

router = routers.DefaultRouter()
router.register('campaings', views.CategoryViewSet, basename='campaings')

urlpatterns = [
    path('', include(router.urls) )
]