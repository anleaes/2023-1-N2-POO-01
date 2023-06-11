from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'vacinationLocal'

router = routers.DefaultRouter()
router.register('local_vacinacao', views.VacinationLocalViewSet, basename='vacinationLocal')

urlpatterns = [
    path('', include(router.urls)),
]