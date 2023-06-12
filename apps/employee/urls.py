from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'employee'

router = routers.DefaultRouter()
router.register('todas', views.EmployeeViewSet, basename='Funcionários')

urlpatterns = [
    path('', include(router.urls) )
]
