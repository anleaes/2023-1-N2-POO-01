from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'localStorage'

router = routers.DefaultRouter()
router.register('estoque_local', views.localStorageViewSet, basename='localStorage')

urlpatterns = [
    path('', include(router.urls) )
]