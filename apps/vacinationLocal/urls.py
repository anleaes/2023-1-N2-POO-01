from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'vacinationLocal'

router = routers.DefaultRouter()
router.register('todos', views.VacinationLocalViewSet, basename='Locais de vacinação')

urlpatterns = [
    path('', include(router.urls)),
]