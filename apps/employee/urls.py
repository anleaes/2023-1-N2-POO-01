from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'employee'

router = routers.DefaultRouter()
router.register('employee', views.ClientViewSet, basename='funcionarios')

urlpatterns = [
    path('', include(router.urls) )
]