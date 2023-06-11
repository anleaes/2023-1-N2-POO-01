from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'vaccinesSupplier'

router = routers.DefaultRouter()
router.register('FornecedorVacina', views.FornecedorVacinaViewSet, basename='FornecedorVacina')

urlpatterns = [
    path('', include(router.urls) )
]
