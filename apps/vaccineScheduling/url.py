from django.urls import path, include
from .views import vaccineschedulingViewSet
from rest_framework import routers

app_name = 'vaccinescheduling'

router = routers.DefaultRouter()
router.register('vaccinescheduling', views.vaccineschedulingViewSet, basename='vaccinescheduling')

urlpatterns = [

    path('', include(router.urls)), 
]